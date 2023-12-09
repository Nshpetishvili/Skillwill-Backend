from django.shortcuts import render

# Create your views here.
from .models import Book

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})