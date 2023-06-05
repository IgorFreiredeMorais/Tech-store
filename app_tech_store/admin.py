from django.contrib import admin

from .models import Product, Category, Manufacturer, Order, OrderItem, Sale, Client
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Sale)
admin.site.register(Client)

# Register your models here.
