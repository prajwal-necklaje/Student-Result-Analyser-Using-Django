from django.db import models

class Ra(models.Model):
    student = models.CharField(max_length=20)
    classes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
