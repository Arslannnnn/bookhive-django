from django.contrib import admin
from .models import Author, Genre, Book, Cart, CartItem, Wishlist

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    search_fields = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'created_at']
    list_filter = ['genres', 'created_at']
    search_fields = ['title', 'author__name']
    filter_horizontal = ['genres']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'book', 'quantity']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    filter_horizontal = ['books']