from django.test import TestCase
from .models import Template

# Create your tests here.

class ProductTests(TestCase):
    
    def test_str(self):
        test_name = Template(title='Test Template')
        self.assertEqual(str(test_name), 'Test Template')
