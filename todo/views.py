from django.shortcuts import render
# Create your views here.


def todolist(request):
    return render(request,'todo/todo.html',{})