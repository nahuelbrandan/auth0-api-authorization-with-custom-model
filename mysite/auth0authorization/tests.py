import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model


class ApplicationTests(TestCase):

    def test_create_app(self):
        User = get_user_model()
        user = User.objects.create_app(username='test', password='test')
        self.assertEqual(user.username, 'test')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_app()
        with self.assertRaises(TypeError):
            User.objects.create_app(username='')
        with self.assertRaises(ValueError):
            User.objects.create_app(username='', password="foo")
