from django.db import models

# Create your models here.
class kakikomiForm(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    body = models.CharField(max_length=100)
