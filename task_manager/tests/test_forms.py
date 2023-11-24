from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from task_manager.forms import (
    TaskForm,
    WorkerPositionUpdateForm, PositionSearchForm, TaskTypeSearchForm, TaskSearchForm, WorkerSearchForm)
from task_manager.models import Position, TaskType


class TaskFormsTests(TestCase):
    def setUp(self):
        # Create some User instances for testing
        self.user1 = get_user_model().objects.create_user(username="user1", password="password1")
        self.user2 = get_user_model().objects.create_user(username="user2", password="password2")

    def test_worker_position_update_form_is_valid(self):
        position = Position.objects.create(name="QA")
        form_data = {
            "position": position.pk,
        }
        form = WorkerPositionUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["position"], position)

    def test_position_search_form_is_valid(self):
        form_data = {
            "name": "Test Position",
        }
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_type_search_form_is_valid(self):
        form_data = {
            "name": "Test Task Type",
        }
        form = TaskTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_search_form_is_valid(self):
        form_data = {
            "name": "Test Task",
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_worker_search_form_is_valid(self):
        form_data = {
            "username": "testuser",
        }
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
