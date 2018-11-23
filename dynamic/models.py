from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class User(AbstractUser):
    comments = models.ForeignKey("Comments", null=True, on_delete=models.CASCADE, related_name='user_comments')
    files = models.ForeignKey("FileExcel", null=True, on_delete=models.CASCADE, related_name='user_files')


class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    content = models.TextField(blank=True, null=True)


class FileExcel(models.Model):
    fid = models.IntegerField(primary_key=True)
    describle = models.TextField(blank=True,null=True)
    uploadtime = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey("Comments", on_delete=models.CASCADE)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    excel = models.FileField(upload_to='excels/')
    downtimes = models.IntegerField(default=0)
    hinttimes = models.IntegerField(default=0)
