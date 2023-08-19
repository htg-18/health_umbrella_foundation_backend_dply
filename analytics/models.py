from django.db import models
from simple_history.models import HistoricalRecords

class test_table(models.Model):
    name = models.CharField(max_length=1000)
    show = models.BooleanField()
    history = HistoricalRecords()

