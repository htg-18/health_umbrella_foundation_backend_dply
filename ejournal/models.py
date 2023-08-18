from django.db import models


class ejournal_table(models.Model):
    name = models.CharField(max_length=1000)
    file = models.FileField(upload_to="ejournal_docs/files/")
    image = models.ImageField(upload_to="ejournal_docs/cover_images/")
    show = models.BooleanField(default=True)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class subscription_table(models.Model):
    email_address = models.EmailField()
    send = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.email_address


class key_value_table(models.Model):
    key = models.CharField(max_length=1000)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.key
