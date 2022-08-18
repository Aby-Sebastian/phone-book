from unicodedata import category
from django.test import TestCase
from app.models import Contact

class ContactTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(first_name='aby', last_name='sebastian',phone_number='9961293331',email_id='aby@gmail.com',favorite=True,category='Home')
    
    def test_contact_first_name(self):
        contact = Contact.objects.get(pk=1)
        
        self.assertEqual(contact.first_name, 'aby')

    def test_contact_last_name(self):
        contact = Contact.objects.get(pk=1)
        
        self.assertEqual(contact.last_name, 'sebastian')
    
    def test_contact_phone_number(self):
        contact = Contact.objects.get(pk=1)
        
        self.assertEqual(contact.phone_number, '9961293331')
    
    def test_contact_favorite(self):
        contact = Contact.objects.get(pk=1)
        
        self.assertEqual(contact.favorite, True)
    
    def test_contact_favorite_false(self):
        contact = Contact.objects.get(pk=1)
        
        self.assertTrue(contact.favorite, True)