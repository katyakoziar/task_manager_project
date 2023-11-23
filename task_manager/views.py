from django.db.models import QuerySet
from django.shortcuts import render
from django.views import generic

from task_manager.models import TaskType, Position, Task, Worker


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_task_types": TaskType.objects.count(),
        "num_positions": Position.objects.count(),
        "num_tasks": Task.objects.count(),
        "num_workers": Worker.objects.count()
    }

    return render(request, "task_manager/index.html", context=context)
