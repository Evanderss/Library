from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, "pages/homepage.html")

def about(request):
    return render(request, "pages/about.html")

def books(request):
    return render(request, "books/index.html")