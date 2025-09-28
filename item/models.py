from django.db import models
from django.contrib.auth.models import User as user
# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = "Catagory"
        verbose_name_plural = "Catagories"

class Item(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items_images', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    created_by = models.ForeignKey(user, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = "Item"
        verbose_name_plural = "Items"