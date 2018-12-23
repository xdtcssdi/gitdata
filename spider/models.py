from django.db import models


# Create your models here.
class ImageItem(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    img = models.CharField(blank=True, null=True, max_length=100)
