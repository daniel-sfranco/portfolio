# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello, World! This is my personal portfolio website.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("I'm a software engineer with a passion for technology and design.")
    return render(request, 'about.html')
