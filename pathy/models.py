from django.db import models
from simple_history.models import HistoricalRecords
from PIL import Image
from django.core.exceptions import ValidationError
from datetime import datetime
import os

def validate_webp_image(value):
    if not value.name.lower().endswith('.webp'):
        raise ValidationError("Only webp images allowed")
    
def validate_small_letters(value):
    if not value.islower():
        raise ValidationError("Only small letters allowed")

def validate_pdf_file(value):
    if not value.name.lower().endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")


class pathy_table(models.Model):
    title = models.CharField(max_length=1000, validators=[validate_small_letters])
    text = models.TextField()
    image = models.ImageField(upload_to="pathy_section_images/", validators=[validate_webp_image])
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # rename the image as name_timestamp.webp
            current_datetime = datetime.now()
            timestamp = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
            current_imagename = os.path.basename(self.image.name)
            name, extension = os.path.splitext(current_imagename)
            self.image.name = f"{name}_{timestamp}{extension}"
        super().save(*args, **kwargs)
    

class effective_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, validators=[validate_small_letters])
    link = models.URLField()
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.pathy}'s {self.name}"
