from django.db import models
from datetime import datetime


class Calculation(models.Model):
    result = models.DecimalField(max_digits=4, decimal_places=2)
    num_one = models.DecimalField(max_digits=4, decimal_places=2)
    num_two = models.DecimalField(max_digits=4, decimal_places=2)
    operator = models.CharField(max_length=1)
    calc_date = models.DateField(default=datetime.now)
