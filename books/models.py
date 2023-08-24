from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    image=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/default.jpg')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    is_available = models.BooleanField(default=True, help_text='Is this book currently available?')
    availability_date = models.DateField(null=True, blank=True, help_text='Date when the book will be available')

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Science Fiction, Mystery, etc.)')

    def __str__(self):
        return self.name



class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.user} borrowed {self.book}"



class BorrowForm(forms.Form):
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
