from django.urls import path, include
from . import views

app_name = "to_do_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:task_id>', views.remove, name='remove'),
    path('complete/<int:task_id>', views.change_status, name='change_status'),
]
