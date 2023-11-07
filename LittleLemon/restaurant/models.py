from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.item} : {str(self.price)}'

class Booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()
