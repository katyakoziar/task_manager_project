from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from task_manager.models import Worker, Task, TaskType, Position


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="adminpassword"
        )
        self.client.force_login(self.admin_user)

    def test_worker_position_displayed_in_list(self):
        position = Position.objects.create(name="Test Position")
        worker = Worker.objects.create(username="testuser", position=position)
        url = reverse("admin:task_manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, worker.position)

    def test_worker_position_displayed_in_detail(self):
        position = Position.objects.create(name="Test Position")
        worker = Worker.objects.create(username="testuser", position=position)
        url = reverse("admin:task_manager_worker_change", args=[worker.id])
        res = self.client.get(url)
        self.assertContains(res, worker.position)
