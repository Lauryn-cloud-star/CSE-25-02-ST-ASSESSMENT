# my_app/admin.py

from django.contrib import admin
from .models import Product

admin.site.register(Product)
