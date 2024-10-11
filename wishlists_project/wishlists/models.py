from django.db import models
from django.contrib.auth.models import User


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name
