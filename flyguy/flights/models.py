from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField()

    class Meta:
        ordering = ('-date',)