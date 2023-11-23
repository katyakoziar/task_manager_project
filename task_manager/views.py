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


class TaskTypeListView(generic.ListView):
    model = TaskType
    queryset = TaskType.objects.order_by("name")
    paginate_by = 5
    template_name = "task_manager/task_type_list.html"
    context_object_name = "task_type_list"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.select_related("task_types")
    paginate_by = 5


class PositionListView(generic.ListView):
    model = Position
    queryset = TaskType.objects.order_by("name")
    paginate_by = 5


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.select_related("positions")
