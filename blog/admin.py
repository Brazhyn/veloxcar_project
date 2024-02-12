from django.contrib import admin
from .models import CarPost, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


# class CarPostAdmin(admin.ModelAdmin):
#     pass


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(CarPost)
