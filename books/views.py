from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Cart, CartItem, Wishlist, Genre


def book_list(request):
    genre_filter = request.GET.get('genre', '')

    if genre_filter:
        books = Book.objects.filter(genres__name=genre_filter)
    else:
        books = Book.objects.all()

    # Получаем все жанры для фильтров
    all_genres = Genre.objects.all()

    return render(request, 'books/book_list.html', {
        'books': books,
        'selected_genre': genre_filter,
        'all_genres': all_genres
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Создаем корзину
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Добавляем книгу в корзину
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'Книга "{book.title}" добавлена в корзину!')
    return redirect('book_detail', book_id=book_id)


@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Создаем список желаний
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    # Добавляем книгу
    wishlist.books.add(book)

    messages.success(request, f'Книга "{book.title}" добавлена в список желаний!')
    return redirect('book_detail', book_id=book_id)


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'books/cart.html', {'cart': cart})


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'books/wishlist.html', {'wishlist': wishlist})