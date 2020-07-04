from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
import os


# Create your models here.
class WordCount(models.Model):
    title = models.CharField(max_length=200)
    app_name = models.CharField(max_length=200)
    comments = models.TextField(default="")
    file = models.FileField(upload_to='WordCount',)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=False)
    words = models.TextField()
    lines = models.CharField(max_length=100)


@receiver(models.signals.post_delete,sender=WordCount)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
