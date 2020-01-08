from django.db import models


# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    Date = models.DateTimeField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'
