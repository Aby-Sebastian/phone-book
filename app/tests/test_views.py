from urllib import response
from django.test import TestCase
from app.models import Contact
from django.urls import reverse

class ViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        :return: None
        """
        no = 20
        for i in range(no):
            Contact.objects.create(first_name='aby{i}', last_name='sebastian{i}',
            phone_number='996129333{i}',email_id='aby{i}@gmail.com',favorite=True,category='Home')

    def test_view_url(self):
        """
        :return: None
        """
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        :return: None
        """
        response = self.client.get(reverse('app:home'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        """
        :return: None
        """
        response = self.client.get(reverse('app:favorite'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'phonebook/favorite.html')

    def test_search_view(self):
        """
        Test search view
        """
        response = self.client.get('/search/?q=aby1', follow=True)
        self.assertEqual(response.status_code, 200)
