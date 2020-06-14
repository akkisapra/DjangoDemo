from django.db import models

class bill(models.Model):
    NMI = models.CharField(max_length=10)
    serial = models.CharField(max_length=12)
    readingValue = models.CharField(max_length=15, blank=True)
    date = models.DateTimeField()
    fileName = models.TextField()


