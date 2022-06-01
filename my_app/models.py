from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __unicode__(self):
        return self.user.name


