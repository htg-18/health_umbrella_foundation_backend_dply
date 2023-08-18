from django.db import models
from PIL import Image
import os
from datetime import datetime
from django.utils import timezone


class testimonial_table(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.heading


class video_table(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to="video_table_images/")
    ytplaylist_link = models.URLField(max_length=300)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.heading


class key_value_table(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.key
