from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Product, User
from django.db.utils import IntegrityError
from django.db import transaction


class TestProductsModel(TestCase):
    def setUp(self):
        self.product = Product()
        self.product.name = 'Test Product'
        self.product.price = 100.00
        self.product.stock = 10

    def test_in_stock(self):
        got = self.product.in_stock
        self.assertTrue(got)
        self.product.stock = 0
        got = self.product.in_stock
        self.assertFalse(got)

    def test_discount_calculation(self):
        got = self.product.calculate_discount(10)
        self.assertEqual(got, 90.00)
        with self.assertRaises(ValueError):
            self.product.calculate_discount(110)
        with self.assertRaises(ValueError):
            self.product.calculate_discount(-10)

    def test_app_level_clean_validation(self):
        self.product.price = -10
        with self.assertRaises(ValidationError):
            self.product.full_clean()

        self.product.stock = -1
        with self.assertRaises(ValidationError):
            self.product.full_clean()

    def test_integrity_constraints(self):
        self.product.price = -1
        self.product.stock = -1
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                self.product.save()

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                self.product.save()
