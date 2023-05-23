from django.db import models

# Create your models here.

class proyectlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    code = models.TextField(default='')
    date = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
