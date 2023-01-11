from django.shortcuts import render
from .models import Book


def books_view(request):
    books_from_db = Book.objects.all()
    books = list()
    for book in books_from_db:
        books.append({
            'name': book.name,
            'author': book.author,
            'pub_date': book.pub_date.strftime('%d-%m-%Y')
        })
        day, month, year = book.pub_date.strftime('%d-%m-%Y').split('-')
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def book_view(request, year, month, day):
    contex = dict()
    books_from_db = Book.objects.all()
    books = list()
    for book in books_from_db:
        if f'{year}-{month}-{day}' == book.pub_date.strftime('%Y-%m-%d'):
            books.append({
                'name': book.name,
                'author': book.author,
                'pub_date': book.pub_date.strftime('%d-%m-%Y')
            })
    dates = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')
    dates = [date.strftime('%Y-%m-%d')for date in dates]
    current_date_index = dates.index(f'{year}-{month}-{day}')
    if current_date_index != 0:
        contex['has_previous_date'] = True
        contex['previous_pub_date'] = dates[current_date_index - 1]
    if current_date_index != len(dates) - 1:
        contex['has_next_date'] = True
        contex['next_pub_date'] = dates[current_date_index + 1]
    contex['books'] = books

    return render(request, 'books/books_list.html', context=contex)


def home(request):
    template = 'base.html'
    return render(request, template)
