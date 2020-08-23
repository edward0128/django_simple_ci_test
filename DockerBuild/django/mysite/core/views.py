from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
import os
import re
import subprocess
from django.core.files.base import ContentFile

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        context['result']=str(name)

    fs = FileSystemStorage()
    fs.save("1234222.txt",ContentFile('new content'))
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    #c=Book.objects.filter(title='e')
    #print(c[0].pdf)
    #print(c[0].title)
    #print(c[0].author)
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):

    

    if request.method == 'POST':

        data = request.POST.copy()
        #print(request.build_absolute_uri())
        #print(request.get_current().domain)

        data['test'] ='http://127.0.0.1:8787/media/books/pdfs2/1234.txt'


        form = BookForm(data, request.FILES)
        
        
        if form.is_valid():
            #print(form.cleaned_data.get('title'))
            #subprocess.run(["touch", "/tmp/dslfjsdlfkjslkfjd"])
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
