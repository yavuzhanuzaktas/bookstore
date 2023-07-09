from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
from django.http import Http404
from .models import Book
# Create your views here.

def index(request):  # index -> default olarak anasayfayı ayarlar.
    return HttpResponse("Anasayfa")

def authors(request):#authors bilgi penceresi
    
    context ={
        'authors_list': Author.objects.all()
    }
    return render(request,'authors.html',context)

def books(request): # books bilgi penceresi

    context={
        'books_list': Book.objects.all()
    }
    return render(request,'books.html',context)

def authorDetails(request,authorId): #query string(authorId)
    try:
        context ={
            'author_detail': Author.objects.get(pk=authorId)
        }
    except Author.DoesNotExist:
        raise Http404("Yazar Bulunamadı")    
    return render(request,'authorDetail.html',context)
