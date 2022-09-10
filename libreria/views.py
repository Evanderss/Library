from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from .forms import bookForm

# Create your views here.
def homepage(request):
    return render(request, "pages/homepage.html")

def about(request):
    return render(request, "pages/about.html")

def books(request):
    books = book.objects.all()
    return render(request, "books/index.html", {"books" : books})

def create(request):
    form = bookForm(request.POST or None)
    return render(request, "books/create.html", { "form": form})

def edit(request):
    return render(request, "books/edit.html")
    