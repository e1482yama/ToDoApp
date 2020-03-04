from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
<<<<<<< HEAD
    model = TodoModel
=======
    model = TodoModel
>>>>>>> abfeadd42205ac956cd97b544da3372668e89847
