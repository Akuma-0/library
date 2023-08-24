from django.shortcuts import render,get_object_or_404, redirect
from .models import Book,Borrow,BorrowForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def allbooks(request):
    books= Book.objects.all()
    return render(request,'books/allbooks.html',{'books': books})


def book(request,id):
    b=get_object_or_404(Book,id=id)
    return render(request, 'books/book.html', context={"b": b})



@login_required
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    if not book.is_available:
        return render(request, 'books/book_not_available.html', {'book': book})
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            return_date = form.cleaned_data['return_date']
            book.is_available = False
            book.availability_date = return_date
            book.save()
            borrow = Borrow(user=request.user, book=book, return_date=return_date)
            borrow.save()
            return redirect(f'/{book_id}/', book_id=book_id)
    else:
        form = BorrowForm()
    return render(request, 'books/borrow_book.html', {'book': book, 'form': form})

@login_required
def user_borrowed_books(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    return render(request, 'books/user_borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def return_book(request, borrow_id):
    borrow = Borrow.objects.get(pk=borrow_id)
    if borrow.user == request.user:
        borrow.book.is_available = True
        borrow.book.save()
        borrow.delete()
        return redirect('user_borrowed_books')
    else:
        # Handle unauthorized access (someone trying to return a book for another user)
        pass
