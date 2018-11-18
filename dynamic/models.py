from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    comments = models.ForeignKey("Comments", on_delete=models.CASCADE)
    files = models.ForeignKey("FileExcel", on_delete=models.CASCADE)


class Comments(models.Model):
    cid = models.IntegerField(max_length=11, unique=True, blank=False, null=False, primary_key=True)
    content = models.TextField(blank=True, null=True)


class FileExcel(models.Model):
    fid = models.IntegerField(unique=True, blank=False, null=False, primary_key=True)
    comments = models.ForeignKey("Comments", on_delete=models.CASCADE)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    excel = models.FileField(upload_to='excels/')
