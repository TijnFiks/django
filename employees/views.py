from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    return redirect('main/index/')