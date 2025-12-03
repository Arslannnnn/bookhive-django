from django.shortcuts import render, get_object_or_404

def book_list(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'book_list': books})

def book_detail(request, book_id):
    from .models import Book
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})