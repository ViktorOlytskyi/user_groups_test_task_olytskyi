from django.test import TestCase
from django.urls import reverse
from .models import User
from ..groups.tests import GroupTests


class UserTests(TestCase):

    def test_add_user_page(self):
        response = self.client.get(reverse('add_user'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new user')

    def test_add_user(self):
        user_count_before = User.objects.count()
        data = {'name': 'Test User', 'group': 1}
        response = self.client.post(reverse('add_user'), data)
        user_count_after = User.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user_count_after, user_count_before + 1)

    def setUp(self):
        group = GroupTests().test_add_group()
        self.user = User.objects.create(name='Test User', group=group)

    def test_edit_user_page(self):
        response = self.client.get(reverse('edit_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test User')

    def test_edit_user(self):
        data = {'name': 'Test User', 'group': 1}
        response = self.client.post(reverse('edit_user', args=[self.user.id]), data)
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_user.name, 'Test User')
        self.assertEqual(updated_user.group_id, 1)
