# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True, default=datetime.now())

    def __unicode__(self):
        return "%s: %s" % (unicode(self.date), self.description)

class Product(models.Model):
    description = models.TextField(default='')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    transaction = models.ForeignKey("Transaction")
    category = models.ForeignKey("Category")

    def __unicode__(self):
        return "%s, %.2f" % (self.description, self.price)

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name
