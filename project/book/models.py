from author.models import Author
from publisher.models import Publisher

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.name} | Authors: {self.author.name}"


class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if self.quantity > 0:
            self.in_stock = True
        else:
            self.in_stock = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.name} - Stock: {self.quantity}"


    @classmethod
    def get_all_in_stock(cls):
        return cls.objects.filter(in_stock=True)
