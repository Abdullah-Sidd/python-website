from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name 