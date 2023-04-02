from django.db import models

class disease_table(models.Model):
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.disease
    
class testimonial_table(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.heading
    
class video_table(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='video_table_images/')
    ytplaylist_link = models.URLField(max_length=300)

    def __str__(self):
        return self.heading
    
class key_value_table(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField(max_length=1000)

    def __str__(self):
        return self.key

