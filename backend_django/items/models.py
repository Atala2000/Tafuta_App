from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description  = models.CharField(max_length=500)
    category = models.CharField(max_length=255, default='default_category')
    location_found = models.CharField(max_length=50, blank=True, null=True)
    date_found = models.DateField()
    image = models.ImageField(upload_to='uploads/' ,default='add_item.png', max_length=100)
    #owner = models.ForeignKey(get_user_model, on_delete=models.CASCADE, related_name='owned_items', null=True, blank=True)

    def __str__(self):
        return self.name



class Credential(Item):
    type = models.CharField(max_length=255)

class Electronic(Item):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

class Clothing(Item):
    pass
    #size= models.CharField(max_length=255)
    #color = models.CharField(max_length=255)


class Pet(Item):
    type = models.CharField(max_length=255)


class Stationary(Item):
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "stationary"

class Furniture(Item):
    type = models.CharField(max_length=255)

    class Meta :
        verbose_name_plural = "furniture"