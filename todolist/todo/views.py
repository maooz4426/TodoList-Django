from django.forms import DateInput
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Task
from .forms import TaskForm
#ログインしていないとviewを表示できないように
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ListView(LoginRequiredMixin,generic.ListView):
    model = Task
    template_name = "todo/task_list.html"

    #コンテキストを加工するメソッド
    def get_context_data(self):
        context = super().get_context_data()

        #prioritykeyに対して降順に表示させるためにorder_by('pk')
        context["completed_tasks"] = Task.objects.filter(completed=True).order_by('pk')
        context["incompleted_tasks"] = Task.objects.filter(completed=False).order_by('pk')
        return context

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Task
    fields = '__all__'

class CreateView(LoginRequiredMixin,generic.edit.CreateView):
    template_name = 'todo/task_form.html'
    form_class = TaskForm

class UpdateView(LoginRequiredMixin,generic.edit.UpdateView):
    template_name = 'todo/task_form.html'
    form_class = TaskForm

    #UpdateView is missing a QuerySet. Define UpdateView.model, UpdateView.queryset, or override UpdateView.get_queryset().
    #解決するためにget_querysetメソッドをオーバーライド
    def get_queryset(self):
        return Task.objects.all()

class DeleteView(LoginRequiredMixin,generic.edit.DeleteView):
    template_name = 'todo/task_confirm_delete.html'
    model = Task

    #reverse_lazyはクラスベースビューで主に使う
    #URLパターンが読み込まれていなくても使える
    #必要になったら指定した先にリダイレクトする
    success_url = reverse_lazy('todo:list')

def complete_task(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.completed = True
    task.save()
    return redirect('todo:list')

def reverse_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.completed = False
    task.save()
    return redirect('todo:list')