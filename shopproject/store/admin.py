from django.contrib import admin
from .models import Category, Product
# Register your models here.

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'created_at']
    readonly_fields =  ['created_at']
    