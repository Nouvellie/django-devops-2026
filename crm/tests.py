from django.test import TestCase
from django.urls import reverse

from .models import DailyNote


class DailyNoteTests(TestCase):

    def test_home_page_loads(self):

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "index.html")

    def test_create_note_model(self):

        note = DailyNote.objects.create(title="Test Note")

        self.assertEqual(note.title, "Test Note")

        self.assertEqual(DailyNote.objects.count(), 1)

    def test_create_note_via_post(self):

        response = self.client.post(reverse("home"), {"title": "Posted note"})

        self.assertEqual(DailyNote.objects.count(), 1)

        self.assertRedirects(response, reverse("home"))
