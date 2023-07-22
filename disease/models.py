from django.db import models


class disease_table(models.Model):
    name = models.CharField(max_length=1000)
    show = models.BooleanField(default=True)
    text = models.TextField()
    summary = models.TextField()
    image_link = models.ImageField(upload_to="disease_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class pathy_table(models.Model):
    PATHY_TYPE_CHOICES = [
        ("therapiesWithDrugs", "therapiesWithDrugs"),
        ("therapiesWithoutDrugs", "therapiesWithoutDrugs"),
        ("lessKnownTherapies", "lessKnownTherapies"),
    ]

    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    show = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=PATHY_TYPE_CHOICES)
    image_link = models.ImageField(upload_to="pathy_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class source_table(models.Model):
    SOURCE_CHOICES = [
        ("books", "books"),
        ("socialMedia", "socialMedia"),
        ("youtube", "youtube"),
        ("website", "website"),
        ("article", "article"),
        ("quora", "quora"),
        ("directCase", "directCase"),
    ]

    name = models.CharField(max_length=1000, choices=SOURCE_CHOICES)
    text = models.TextField()
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class sex_table(models.Model):
    sex = models.CharField(max_length=1000)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.sex


class book_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    rating = models.IntegerField()
    text = models.TextField()
    image_link = models.ImageField(upload_to="book_images/")
    buy_link = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class summary_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.disease} {self.pathy}'s summary"


class data_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    source = models.ForeignKey(source_table, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=2000)
    summary = models.TextField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.disease} {self.pathy} {self.source} {self.pk}"


class case_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    summary = models.TextField()
    rating = models.IntegerField()
    comment = models.TextField()
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    sex = models.ForeignKey(sex_table, on_delete=models.CASCADE)
    age = models.IntegerField()
    occupation = models.CharField(max_length=1000)
    email_address = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=50)
    street_address = models.CharField(max_length=1000)
    zip_code = models.CharField(max_length=50)
    state = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    history_link = models.URLField(max_length=2000)
    allergies_link = models.URLField(max_length=2000)
    reports_link = models.URLField(max_length=2000)
    show = models.BooleanField(default=True)
    show_name = models.BooleanField(default=False)
    show_email = models.BooleanField(default=False)
    show_phone_number = models.BooleanField(default=False)
    show_address = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.disease} {self.pathy} {self.pk}"


class whatsapp_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    key = models.CharField(max_length=2000)
    value = models.TextField()
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.key
