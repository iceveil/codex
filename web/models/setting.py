from django.db import models

class Setting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()