from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .models import Clinets

# Create your views here.


def index(request):
    client = Clinets.objects.all()
    return render(request, "main/index.html", {"title": "main page", "clients": client})


def about(request):
    return render(request, "main/about.html")
