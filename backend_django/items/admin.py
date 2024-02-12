from django.contrib import admin
from .models import Item, Credential, Electronic, Clothing, Pet, Stationary, Furniture

# Register your models here.
admin.site.register(Item)
admin.site.register(Credential)
admin.site.register(Electronic)
admin.site.register(Clothing)
admin.site.register(Pet)
admin.site.register(Stationary)
admin.site.register(Furniture)
