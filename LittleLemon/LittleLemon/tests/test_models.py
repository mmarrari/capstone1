from django.test import TestCase
from restaurant.models import Menu
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(item="Item", price=80)
        self.assertEqual(str(item), "Item : 80")