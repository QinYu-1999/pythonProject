from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=16)
    count = models.IntegerField()
