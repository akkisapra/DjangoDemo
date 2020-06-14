from django.db import models

class bill(models.Model):
    NMI = models.CharField(max_length=10)
    serial = models.CharField(max_length=10)
    readingValue = models.CharField(max_length=10, blank=True)
    date = models.DateTimeField()
    fileName = models.TextField()


