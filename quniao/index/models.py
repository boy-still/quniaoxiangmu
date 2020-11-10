from django.db import models

# Create your models here.
class Quniaodata(models.Model):
    time = models.CharField(max_length=10)
    year = models.IntegerField()
    month = models.TextField()
    day = models.TextField()
    hour = models.TextField()
    min = models.TextField()

class quniao(models.Model):
    time = models.CharField(max_length=10)