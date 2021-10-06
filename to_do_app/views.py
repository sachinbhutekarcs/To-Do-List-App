from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from to_do_app.models import *
from to_do_app.forms import *

# Create your views here

date = datetime.datetime.now()
weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")


def index(request):
    # Query database for tasks
    tasks = Task.objects.all()
    form = NewTaskForm()
    if request.method == "POST":
        # take all the data posted from frontend via post request and store it variable 'form'
        form = NewTaskForm(request.POST)
        # check if data is valid or not
        if form.is_valid():
            # clean the data
            task = form.cleaned_data['name']
            # append list
            Task(name=task, status=False).save()
            # after New task is added, redirect to index page
            # reverse() function figures out the url for path named 'index' in the 'tasks' app
            return HttpResponseRedirect(reverse("to_do_app:index"))
        else:
            # else return the form as invalid data is submitted
            return render(request, "to_do_app/add.html", {
                "form": form,
                "message": "INVALID DATA"
            })

    return render(request, "to_do_app/index.html", {
        # pass the list of tasks for this perticular session
        "tasks": tasks,
        "date": date,
        "form": form,
        "weekday": weekdays[date.weekday()]
    })


def change_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse("to_do_app:index"))


def remove(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("to_do_app:index"))
