from statistics import mode
from django.db import models


class Dummy(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Dummy"
        verbose_name_plural = "Dummies"

    def __str__(self):
        return self.name
