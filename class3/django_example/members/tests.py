
from django.test import TestCase
from django.urls import reverse
from .models import Member  # Ensure this import statement is correct

class MemberModelTests(TestCase):
    def setUp(self):
        Member.objects.create(name="John Doe", email="john@example.com")

    def test_member_creation(self):
        """Test that a member can be created"""
        member = Member.objects.get(name="John Doe")
        self.assertEqual(member.email, "john@example.com")

class MemberViewTests(TestCase):
    def setUp(self):
        self.member = Member.objects.create(name="Jane Doe", email="jane@example.com")

    def test_member_list_view(self):
        """Test the member list view"""
        response = self.client.get(reverse('member_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.member.name)

    def test_member_detail_view(self):
        """Test the member detail view"""
        response = self.client.get(reverse('member_detail', args=[self.member.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.member.name)
        self.assertContains(response, self.member.email)

