from django.db import models
from django.core.exceptions import ValidationError
import re

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def validate_positive_number(self, value, field_name):
        if value <= 0:
            raise ValidationError(f"{field_name} must be positive")

class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'
        app_label = 'main'

    def clean(self):
        if not self.name:
            raise ValidationError("Name cannot be empty")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Invalid email format")

class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'
        app_label = 'main'

    def clean(self):
        if not self.name:
            raise ValidationError("Name cannot be empty")
        self.validate_positive_number(self.price, "Price")

class Order(BaseModel):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'orders'
        app_label = 'main'

    def clean(self):
        self.validate_positive_number(self.quantity, "Quantity")