from django.db import models


class TodoM(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
