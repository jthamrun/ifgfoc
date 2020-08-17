from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.



class connectForm(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phoneNumber = models.PositiveIntegerField()
    email = models.CharField(max_length=40)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50, blank=True)
    addressCity = models.CharField(max_length=20)
    addressState = models.CharField(max_length=20)
    addressZip = models.PositiveIntegerField()
    addressCountry = models.CharField(max_length=20)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    class Meta:
        verbose_name = 'Connect Card'

class prayerForm(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phoneNumber = models.PositiveIntegerField()
    email = models.CharField(max_length=40)
    prayerRequests = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    class Meta:
        verbose_name = 'Prayer Card'
