from django.db import models

class Tariff(models.Model):
    name = models.CharField(max_length=24)
    price = models.IntegerField()
    period = models.IntegerField()

    def __str__(self):
        return f'{self.name}'