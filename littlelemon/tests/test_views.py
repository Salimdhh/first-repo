from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizaa",price=50)
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = response.json()  
        self.assertEqual(len(menus), 3)  
        self.assertEqual(menus[0]['name'], 'Pizza')
    
    