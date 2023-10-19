from django.test import TestCase
from django.urls import reverse
from .models import Group


class GroupTests(TestCase):
    serialized_rollback = True
    def setUp(self):
        self.group = Group.objects.create(name='Test Group', description='Test Description')

    def test_add_group_page(self):
        response = self.client.get(reverse('add_group'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new group')

    def test_add_group(self):
        group = Group.objects.create(name='Test Group')
        group_count_before = Group.objects.count()
        data = {'name': 'Test Group', 'description': 'Test Description'}
        response = self.client.post(reverse('add_group'), data)
        group_count_after = Group.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(group_count_after, group_count_before + 1)

        new_group = Group.objects.last()
        self.assertEqual(new_group.name, 'Test Group')
        self.assertEqual(new_group.description, 'Test Description')
        return group
    def test_edit_group_page(self):
        response = self.client.get(reverse('edit_group', args=[self.group.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit group')

    def test_edit_group(self):
        data = {'name': 'Updated Group', 'description': 'Updated Description'}
        response = self.client.post(reverse('edit_group', args=[self.group.id]), data)
        updated_group = Group.objects.get(id=self.group.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_group.name, 'Updated Group')
        self.assertEqual(updated_group.description, 'Updated Description')
