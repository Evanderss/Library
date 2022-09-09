from struct import pack
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("about", views.about, name="about"),
    path("books", views.books, name="books"),
    path("books/create", views.create, name="create")
]
