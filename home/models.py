from django.db import models
from PIL import Image
import os
from datetime import datetime
from django.utils import timezone


class disease_table(models.Model):
    disease = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.disease


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
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.heading

    def save(self, *args, **kwargs):
        # rename the image if it is present
        # check if the object is being made first time
        if self.image and (self.pk is None):
            # Open the uploaded image file and get the filename and extension
            img = Image.open(self.image)
            filename, extension = os.path.splitext(self.image.name)

            # Generate a new filename using the object's ID and the original file extension
            now = datetime.now()
            formatted_datetime = now.strftime("%Y-%m-%d_%H:%M:%S")
            new_filename = "timage_{}{}".format(formatted_datetime, extension)

            # Set the object's image field to the new filename
            self.image.name = new_filename

            # we can use this to resize the image
            # if img.width > 1000 or img.height > 1000:
            #     max_size = (1000, 1000)
            #     img.thumbnail(max_size)
            #     img.save(self.image.path)
        super().save(*args, **kwargs)


class key_value_table(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.key
