from django.db import models
from django.contrib.auth.models import User

class BookModel(models.Model):
    book_img = models.ImageField(upload_to='images/')
    book_name = models.CharField(max_length=100, verbose_name="Book Name")
    author_name = models.CharField(max_length=100, verbose_name="Author Name")
    book_description = models.TextField(max_length=200, verbose_name="Description")
    book_price = models.CharField(max_length=50, verbose_name="Price")
    book_stock = models.CharField(max_length=50, verbose_name="Stock")
    
    def __str__(self):
        return f"{self.book_name} - {self.author_name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)