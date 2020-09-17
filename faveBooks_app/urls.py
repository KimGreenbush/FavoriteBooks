from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('register/', views.register),
    path('login/', views.login),
    path('books/', views.books),
    path('books/add/', views.add_book),
    path('books/<int:book_id>/delete/', views.delete_book),
    path('books/<int:book_id>/update/', views.update_book),
    path('books/<int:book_id>/favorite/', views.add_to_favorite),
    path('books/<int:book_id>/unfavorite/', views.remove_from_favorite),
    path('books/<int:book_id>', views.book_info),
    path('home/', views.homepage)
]
