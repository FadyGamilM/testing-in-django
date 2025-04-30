from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.


class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    @property
    def in_stock(self) -> bool:
        return self.stock > 0

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')

        if self.stock < 0:
            raise ValidationError('Stock cannot be negative.')

    def calculate_discount(self, discount_percentage: float) -> float:
        if not (0 <= discount_percentage <= 100):
            raise ValueError('Discount percentage must be between 0 and 100.')
        return self.price * (1 - (discount_percentage / 100))
