from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description  = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    location_found = models.CharField(max_length=50, blank=True, null=True)
    date_found = models.DateField()
    image = models.ImageField(upload_to='uploads/' ,default='add_item.png', max_length=100)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_items', null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.name
