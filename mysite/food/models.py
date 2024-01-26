from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_descr = models.CharField(max_length=250)
    price = models.IntegerField()
    item_img = models.CharField(max_length=1000, default="https://alllocal.ca/wp-content/uploads/2020/11/food-placeholder.png")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})