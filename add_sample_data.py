import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookhive_project.settings')
django.setup()

from books.models import Author, Genre, Book
from django.contrib.auth.models import User

# Очищаем старые данные
Book.objects.all().delete()
Author.objects.all().delete()
Genre.objects.all().delete()

# Создаем авторов
authors = [
    Author.objects.create(name="Фёдор Достоевский", bio="Русский писатель, мыслитель"),
    Author.objects.create(name="Лев Толстой", bio="Русский писатель"),
    Author.objects.create(name="Джордж Оруэлл", bio="Британский писатель"),
    Author.objects.create(name="Рэй Брэдбери", bio="Американский фантаст"),
    Author.objects.create(name="Агата Кристи", bio="Английская писательница"),
    Author.objects.create(name="Джоан Роулинг", bio="Британская писательница"),
    Author.objects.create(name="Стивен Кинг", bio="Американский писатель"),
    Author.objects.create(name="Антон Чехов", bio="Русский писатель, драматург"),
]

# Создаем жанры
genres = [
    Genre.objects.create(name="Роман"),
    Genre.objects.create(name="Фантастика"),
    Genre.objects.create(name="Детектив"),
    Genre.objects.create(name="Фэнтези"),
    Genre.objects.create(name="Классика"),
    Genre.objects.create(name="Ужасы"),
    Genre.objects.create(name="Драма"),
    Genre.objects.create(name="Антиутопия"),
]

# Создаем книги
books_data = [
    {
        "title": "Преступление и наказание",
        "author": authors[0],
        "description": "Роман о студенте Раскольникове, совершившем убийство старухи-процентщицы.",
        "price": 499,
        "genres": [genres[0], genres[4]]
    },
    {
        "title": "1984",
        "author": authors[2],
        "description": "Антиутопический роман о тоталитарном обществе под контролем Большого Брата.",
        "price": 399,
        "genres": [genres[1], genres[7]]
    },
    {
        "title": "Война и мир",
        "author": authors[1],
        "description": "Роман-эпопея, описывающий русское общество в эпоху войн против Наполеона.",
        "price": 799,
        "genres": [genres[0], genres[4]]
    },
    {
        "title": "451° по Фаренгейту",
        "author": authors[3],
        "description": "Антиутопия о обществе, где книги находятся под запретом.",
        "price": 349,
        "genres": [genres[1], genres[7]]
    },
    {
        "title": "Гарри Поттер и философский камень",
        "author": authors[5],
        "description": "Первая книга серии о юном волшебнике Гарри Поттере.",
        "price": 599,
        "genres": [genres[3], genres[1]]
    },
    {
        "title": "Убийство в «Восточном экспрессе»",
        "author": authors[4],
        "description": "Знаменитый детектив Эркюля Пуаро расследует убийство в поезде.",
        "price": 299,
        "genres": [genres[2]]
    },
    {
        "title": "Оно",
        "author": authors[6],
        "description": "Роман ужасов о древнем зле, терроризирующем город Дерри.",
        "price": 699,
        "genres": [genres[5], genres[1]]
    },
    {
        "title": "Скотный двор",
        "author": authors[2],
        "description": "Сатирическая повесть-притча о животных, свергнувших своих хозяев.",
        "price": 249,
        "genres": [genres[7], genres[6]]
    },
    {
        "title": "Вишнёвый сад",
        "author": authors[7],
        "description": "Пьеса о судьбе дворянской семьи и их вишнёвого сада.",
        "price": 199,
        "genres": [genres[6], genres[4]]
    },
    {
        "title": "Сияние",
        "author": authors[6],
        "description": "Роман о писателе, который становится смотрителем отеля и сходит с ума.",
        "price": 549,
        "genres": [genres[5], genres[0]]
    },
]

for data in books_data:
    book = Book.objects.create(
        title=data["title"],
        author=data["author"],
        description=data["description"],
        price=data["price"]
    )
    book.genres.set(data["genres"])
    book.save()

print("=" * 50)
print("✅ Создано успешно!")
print(f"📚 Книг: {Book.objects.count()}")
print(f"👤 Авторов: {Author.objects.count()}")
print(f"🏷️ Жанров: {Genre.objects.count()}")
print("=" * 50)