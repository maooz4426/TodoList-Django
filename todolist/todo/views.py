from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Task

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ListView(generic.ListView):
    model = Task
    template_name = "task_list.html"