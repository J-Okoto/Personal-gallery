from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =100, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        
        
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    
    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length =80, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
        self.delete()
    
