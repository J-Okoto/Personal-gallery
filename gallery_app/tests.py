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

