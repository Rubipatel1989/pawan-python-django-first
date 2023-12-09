from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {
        "id":1,
        "name": "Pawan Kumar",
        "age":32
    },
    {
        "id":2,
        "name": "Manoj Kumar",
        "age":32
    },
    {
        "id":3,
        "name": "Rahul Kumar",
        "age":32
    }
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request,'room.html', {'rooms': rooms})