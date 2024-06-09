from django.contrib import admin
from .models import Cart, Customer, Product


# Register your models here.
@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'product_image', 'discounted_price', 'category']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'locality', 'city', 'state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity']

