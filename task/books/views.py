from django.views import View
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages

class AddTask(View):
    def get(self, request):
        form_instance = TaskForm()
        context = {"form": form_instance}
        return render(request, "addtask.html")

    def post(self, request):
        form_instance = TaskForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, "Task added successfully!")
            return redirect("addtask")
        context = {"form": form_instance}
        return render(request, "addtask.html",context)
