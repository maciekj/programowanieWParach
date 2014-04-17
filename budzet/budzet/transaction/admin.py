from django.contrib import admin

# Register your models here.
from .models import Transaction, Product, Category

admin.site.register(Transaction)
admin.site.register(Product)
admin.site.register(Category)