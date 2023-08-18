from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

SOURCE_NAME_LIST = ["books", "socialMedia", "youtube", "website", "article", "quora", "directCase"]
SOURCE_CHOICES = []
for name in SOURCE_NAME_LIST:
    SOURCE_CHOICES.append((name, name))
SOURCE_NAME_LIST.remove('directCase')


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
        return f"{self.name} ({self.disease.name})"


class source_table(models.Model):
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
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, 'rating should be greater than or equal to 1'),
            MaxValueValidator(10, 'rating should be less than or equal to 10')
        ]
    )
    text = models.TextField()
    image_link = models.ImageField(upload_to="book_images/")
    buy_link = models.URLField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return self.name


class summary_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.pathy}'s summary"


class data_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    source = models.ForeignKey(source_table, on_delete=models.CASCADE, limit_choices_to={'name__in': SOURCE_NAME_LIST})
    show = models.BooleanField(default=True)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=2000)
    summary = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, 'rating should be greater than or equal to 1'),
            MaxValueValidator(10, 'rating should be less than or equal to 10')
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at",]  # ordered by decending timestamp

    def __str__(self):
        return self.title


class case_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    summary = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, 'rating should be greater than or equal to 1'),
            MaxValueValidator(10, 'rating should be less than or equal to 10')
        ]
    )
    comment = models.TextField()
    first_name = models.CharField(max_length=1000, null=True)
    last_name = models.CharField(max_length=1000, null=True)
    sex = models.ForeignKey(sex_table, on_delete=models.CASCADE)
    age = models.IntegerField(
        validators=[
            MinValueValidator(1, 'age should be greater than or equal to 1'),
        ],
        null=True
    )
    occupation = models.CharField(max_length=1000, null=True)
    email_address = models.CharField(max_length=1000, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    street_address = models.CharField(max_length=1000, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=1000, null=True)
    country = models.CharField(max_length=1000, null=True)
    history_link = models.URLField(max_length=2000, null=True)
    allergies_link = models.URLField(max_length=2000, null=True)
    reports_link = models.URLField(max_length=2000, null=True)
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
        return f"{self.pathy} {self.pk}"


class whatsapp_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    link = models.URLField(default="healthumbrella.org")
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # ordered by decending timestamp

    def __str__(self):
        return f"{self.pathy}"
