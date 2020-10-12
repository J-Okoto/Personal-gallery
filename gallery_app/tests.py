from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt
# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location= Location(name = 'Nairobi')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(name = 'portrait')

    def test_instance(self):
        self.assertTrue(isinstance(self.cat1, Category))    

    def test_save_category(self):
        self.cat1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.cat1.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)  

    

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

