from django.db.models import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
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


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.select_related("task_type")
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class PositionListView(generic.ListView):
    model = Position
    queryset = Position.objects.order_by("name")
    paginate_by = 5


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.select_related("position")


class WorkerDetailView(generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("tasks")


class WorkerPositionUpdateView(generic.UpdateView):
    model = Worker
    # form_class = WorkerPositionUpdateForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("")
