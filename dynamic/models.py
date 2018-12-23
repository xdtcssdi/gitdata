from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone
import hashlib
import os
import time

class User(AbstractUser):
    comments = models.ForeignKey("Comments", null=True, on_delete=models.CASCADE, related_name='user_comments')
    files = models.ForeignKey("FileExcel", null=True, on_delete=models.CASCADE, related_name='user_files')

class Comments(models.Model):
    cid = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)


def handle_uploaded_file(instance, filename):
    # print(obj.name)
    t = time.time()

    data = filename + str(int(round(t * 1000)))

    tt = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

    name = str(tt)[:20] + '.' + filename.split('.')[-1]

    return 'excels/'+name


class FileExcel(models.Model):
    fid = models.AutoField(primary_key=True)
    pname = models.TextField(blank=True, null=True)
    describle = models.TextField(blank=True, null=True)
    uploadtime = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey("Comments", null=True, on_delete=models.CASCADE)
    user = models.ForeignKey("User", null=True, on_delete=models.CASCADE)
    excel = models.FileField(upload_to=handle_uploaded_file)
    downtimes = models.IntegerField(default=0)
    hinttimes = models.IntegerField(default=0)
