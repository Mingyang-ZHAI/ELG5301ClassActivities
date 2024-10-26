from django.db import models

# Create your models here.
# members/models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name