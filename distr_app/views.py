from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    context = {
        'categories': Category.objects.all(),
        'books':Book.objects.all(),
        'form': BookForm(),
        'categoryform':CategoryForm(),
        'allbook': Book.objects.filter(active=True).count(),
        'soldbook': Book.objects.filter(status='sold').count(),
        'rentedbook': Book.objects.filter(status='rented').count(),
        'availablebook': Book.objects.filter(status='available').count(),
    }
    return render(request,'pages/index.html',context)

def books(request):
    context = {
        'categories': Category.objects.all(),
        'books':Book.objects.all(),
    }
    return render(request,'pages/books.html',context)

def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method == 'POST':
        book_update = BookForm(request.POST, request.FILES, instance=book_id)
        if book_update.is_valid():
            book_update.save()
            return redirect('/')
    else:
        book_update= BookForm(instance=book_id)
    context = {
        'updateform': book_update,
    }
    return render(request,'pages/update.html',context)

# def delete(request):
#     return render(request,'pages/delete.html')