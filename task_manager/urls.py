from django.urls import path

from task_manager.views import (
    index,
    TaskTypeListView,
    PositionListView,
    TaskListView,
    WorkerListView
)

urlpatterns = [
    path("", index, name="index"),
    path("task-types/", TaskTypeListView(), name="task-type-list"),
    path("positions/", PositionListView(), name="position-list"),
    path("tasks/", TaskListView(), name="task-list"),
    path("workers/", WorkerListView(), name="worker-list")
]

app_name = "task_manager"
