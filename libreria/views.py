from django.shortcuts import render, redirect
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
    form = bookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("books")
    return render(request, "books/create.html", { "form": form})

def edit(request, id):
    Book = book.objects.get(id=id)
    form = bookForm(request.POST or None, request.FILES or None, instance=Book)
    return render(request, "books/edit.html", {"form": form})

def delete(request, id):
    Book = book.objects.get(id=id)
    Book.delete()
    return redirect("books")