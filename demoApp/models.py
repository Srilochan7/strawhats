# demoApp/models.py

from django.db import models

class Product(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add any other fields you need for your product model

    def __str__(self):
        return self.name
