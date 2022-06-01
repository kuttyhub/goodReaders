from django.contrib import admin

# Register your models here.
from django.contrib import admin

from my_app.models import User, Author, Product, Order
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Order)