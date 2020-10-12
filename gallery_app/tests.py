from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt
# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc1= Location(name = 'Nairobi')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(name = 'wedding')

    

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new image and saving it
        self.image1= Location(name = 'India')
        self.image1.save_location()

        self.category = Category(name='portrait')
        self.category.save_category()
        
        self.new_image= Image(name = 'oldman',description='this is a test image', location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))


    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

