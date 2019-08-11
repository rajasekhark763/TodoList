from django.shortcuts import render
from todoapp.models import Todo
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class TodoListView(ListView):
    model=Todo

class TodoDetailView(DetailView):
    model=Todo

class TodoCreateView(CreateView):
    model=Todo
    fields=('title','description','status','date_time')

class TodoUpdateView(UpdateView):
    model=Todo
    fields=('description','status','date_time')

class TodoDeleteView(DeleteView):
    model=Todo
    success_url=reverse_lazy('todos')
