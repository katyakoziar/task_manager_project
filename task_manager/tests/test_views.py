from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse

from task_manager.models import TaskType, Position, Worker, Task


class TaskManagerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse("task_manager:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/index.html")

    def test_task_type_list_view(self):
        TaskType.objects.create(name="Type 1")
        TaskType.objects.create(name="Type 2")
        response = self.client.get(reverse("task_manager:task-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_type_list.html")

    def test_task_type_create_view(self):
        response = self.client.get(reverse("task_manager:task-type-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_type_form.html")

    def test_task_type_update_view(self):
        task_type = TaskType.objects.create(name="Type 1")
        response = self.client.get(reverse(
            "task_manager:task-type-update",
            args=[task_type.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_type_form.html")

    def test_task_type_delete_view(self):
        task_type = TaskType.objects.create(name="Type 1")
        response = self.client.get(reverse(
            "task_manager:task-type-delete",
            args=[task_type.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "task_manager/task_type_confirm_delete.html"
        )

    def test_task_list_view(self):
        task_type = TaskType.objects.create(name="Some Task Type")
        Task.objects.create(
            name="Task 1",
            description="Description 1",
            deadline="2023-12-31",
            is_completed=False,
            task_type=task_type
        )
        Task.objects.create(
            name="Task 2",
            description="Description 2",
            deadline="2023-12-31",
            is_completed=True,
            task_type=task_type
        )
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/task_list.html")

    def test_worker_list_view(self):
        Position.objects.create(name="Position 1")
        Worker.objects.create(
            username="worker1",
            position=Position.objects.first()
        )
        Worker.objects.create(
            username="worker2",
            position=Position.objects.first()
        )
        response = self.client.get(reverse("task_manager:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/worker_list.html")
