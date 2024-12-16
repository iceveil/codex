from django.db import models

from web.models.box import Box
from web.models.user import User


class Code(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    fileType = models.CharField(max_length=255)
    fileSize = models.IntegerField()
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
