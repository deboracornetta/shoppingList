from django.db import models


class ShoppingList(models.Model):
    bought = models.BooleanField(default=False)
    item_to_buy = models.CharField(max_length=50)

    def __str__(self):
        return self.item_to_buy
