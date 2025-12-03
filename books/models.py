# books/models.py
from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя автора")
    bio = models.TextField(blank=True, verbose_name="Биография")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название жанра")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    genres = models.ManyToManyField(Genre, related_name='books', verbose_name="Жанры")
    description = models.TextField(verbose_name="Описание")
    cover_image = models.ImageField(upload_to='books/covers/', default='default_book_cover.jpg', verbose_name="Обложка")
    published_date = models.DateField(null=True, blank=True, verbose_name="Дата публикации")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.title} ({self.author.name})"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    text = models.TextField(verbose_name="Текст рецензии")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"
        unique_together = [['book', 'user']]
        ordering = ['-created_at']

    def __str__(self):
        return f'Рецензия {self.user.username} на "{self.book.title}"'


class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='in_collections')
    STATUS_CHOICES = [
        ('RD', 'Прочитано'),
        ('RG', 'Читаю сейчас'),
        ('WT', 'Хочу прочитать'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="Статус")
    added_to_collection_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга в коллекции"
        verbose_name_plural = "Книги в коллекциях"
        unique_together = [['user', 'book']]
        ordering = ['-added_to_collection_at']

    def __str__(self):
        return f'{self.book.title} - {self.get_status_display()} у {self.user.username}'