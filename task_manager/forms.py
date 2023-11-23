from django import forms
from django.contrib.auth import get_user_model

from task_manager.models import Worker


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["position"]
