from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.


class Ticket(models.Model):
    day = models.DateField()
    time = models.TimeField()
    departure_port = models.CharField(max_length=5)
    arrival_port = models.CharField(max_length=5)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    ticket_type = models.CharField(max_length=25, default='Normal')
    sit_class = models.CharField(max_length=20, default='Trevaler')
    carrier = models.CharField(max_length=5, default='Aiur')
    date_created = models.DateTimeField()

    def __str__(self):
        return str(self.id) + " " + (str(self.date_created) if self.date_created is not None else 'None')
