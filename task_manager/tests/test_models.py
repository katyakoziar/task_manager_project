from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from task_manager.models import Position, TaskType, Worker, Task


class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create(username="testuser", position=self.position)
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.task = Task.objects.create(
            name="Fix critical bug",
            description="Fix a critical bug in the system",
            deadline=timezone.now().date() + timezone.timedelta(days=7),
            priority="High",
            task_type=self.task_type
        )
        self.task.assignees.add(self.worker)

    def test_task_type_str(self):
        task_type = TaskType.objects.get(name="Bug Fix")
        self.assertEqual(str(task_type), "Bug Fix")

    def test_position_str(self):
        position = Position.objects.get(name="Manager")
        self.assertEqual(str(position), "Manager")

    def test_task_str(self):
        expected_str = f"{self.task.name}, {self.task.deadline}"
        self.assertEqual(str(self.task), expected_str)

    def test_task_clean_method_future_deadline(self):
        self.task.deadline = timezone.now().date() + timezone.timedelta(days=14)
        self.task.clean()

    def test_task_clean_method_past_deadline(self):
        self.task.deadline = timezone.now().date() - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.task.clean()
