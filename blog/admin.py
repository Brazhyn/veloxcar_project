from django.contrib import admin
from .models import CarPost, Category


# class CategoryAdmin(admin.ModelAdmin):
#     pass


# class CarPostAdmin(admin.ModelAdmin):
#     pass


# Register your models here.
admin.site.register(Category)
admin.site.register(CarPost)
