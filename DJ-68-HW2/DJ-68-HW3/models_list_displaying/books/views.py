from django.shortcuts import render, Http404, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def publish_book(request, pub_date):
    books = Book.objects.all()
    current_book = books.filter(pub_date=pub_date)
    if not current_book:
        raise Http404()
    next_book = books.filter(pub_date__gt=pub_date).first()
    prev_book = books.filter(pub_date__lt=pub_date).last()
    context = {"books": current_book, 'next_book': next_book, 'prev_book': prev_book}
    return render(request, 'books/book_publish.html', context)
