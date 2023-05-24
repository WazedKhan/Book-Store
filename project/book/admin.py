from django.contrib import admin

from .models import Book, Stock

admin.site.register(Book)
admin.site.register(Stock)
