from django.urls import path
from . import views

urlpatterns = [
path('', views.allbooks),
path('<int:id>/', views.book, name='book.show'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('borrowed-books/', views.user_borrowed_books, name='user_borrowed_books'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
    ]