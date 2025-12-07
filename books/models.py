from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя автора")
    bio = models.TextField(blank=True, verbose_name="Биография")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Цена")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Обложка")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} - {self.author.name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
        unique_together = ['cart', 'book']

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"

    def total_price(self):
        return self.quantity * self.book.price


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    books = models.ManyToManyField(Book, related_name='wishlisted_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Список желаний"
        verbose_name_plural = "Списки желаний"

    def __str__(self):
        return f"Список желаний {self.user.username}"