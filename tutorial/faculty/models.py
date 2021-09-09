from django.db import models

class Faculty(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
