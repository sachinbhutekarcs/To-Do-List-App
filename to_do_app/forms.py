from django import forms
from to_do_app.models import Task


class NewTaskForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Add New Task'}))

    class Meta:
        model = Task
        fields = ['name']
