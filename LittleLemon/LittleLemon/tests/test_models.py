from django.tests import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
     def test_get_item(self):
         item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
         self.assertEqual(item, "IceCream : 80")