from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField()
    owner = models.ForeignKey(User, related_name='flights')

    class Meta:
        ordering = ('-date',)
