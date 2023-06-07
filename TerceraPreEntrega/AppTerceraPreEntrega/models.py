from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=256)
    last_name  = models.CharField(max_length=256)
    email      = models.EmailField(blank=True)
    phone      = models.CharField(max_length=20, blank=True)    

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Seller(models.Model):
    username     = models.CharField(max_length=15)
    first_name   = models.CharField(max_length=256)
    last_name    = models.CharField(max_length=256)
    email        = models.EmailField(blank=True)
    phone        = models.CharField(max_length=20, blank=True)
    birthday_day = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Product(models.Model):
    name  = models.CharField(max_length=30)
    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.brand}, {self.price}, {self.stock}"

class Sale(models.Model):
    username    = models.ForeignKey(Seller, on_delete=models.CASCADE)
    client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount      = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.username}, {self.client}, {self.product}, {self.amount}"