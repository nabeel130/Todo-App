from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    context = {
        'all_items' : all_todo_items
    }
    return render(request , "todo.html" , context);