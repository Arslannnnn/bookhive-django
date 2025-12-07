from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('<int:book_id>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('cart/', views.view_cart, name='view_cart'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
]