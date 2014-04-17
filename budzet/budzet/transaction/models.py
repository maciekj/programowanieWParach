from django.db import models
from django.conf import settings
# Create your models here.



class Transaction(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField()


class Product(models.Model):
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    transaction = models.ForeignKey("Transaction")
    category = models.ForeignKey("Category")


class Category(models.Model):
    name = models.CharField(max_length=80)
