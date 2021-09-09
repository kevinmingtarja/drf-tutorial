from django.db import models

class Student(models.Model):
    nusnet_id = models.CharField(primary_key=True, max_length=16, blank=False, unique=True)
    name = models.CharField(max_length=128, blank=False)
    year = models.PositiveIntegerField(blank=False)
