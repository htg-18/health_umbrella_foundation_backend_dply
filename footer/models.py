from django.db import models
from django.utils import timezone
from datetime import datetime


class footer_table(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.key
