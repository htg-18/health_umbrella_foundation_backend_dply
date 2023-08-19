from django.db import models

class pathy_table(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    image = models.ImageField(upload_to="pathy_section_images/")
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.title
    

class effective_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    link = models.URLField()
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.pathy}'s {self.name}"
