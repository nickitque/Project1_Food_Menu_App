from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_descr = models.CharField(max_length=250)
    price = models.IntegerField()

