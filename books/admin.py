from django.contrib import admin
from .models import Author, Genre, Book, Review, Collection

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'added_at')
    list_filter = ('genres', 'added_at')
    search_fields = ('title', 'author__name')
    filter_horizontal = ('genres',)  # Удобный виджет для ManyToMany
    readonly_fields = ('added_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title', 'user__username')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'added_to_collection_at')
    list_filter = ('status', 'added_to_collection_at')