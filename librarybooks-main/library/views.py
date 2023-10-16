from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import books, UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .serializers import Bookserializer


def login(request):
    return HttpResponseRedirect("/accounts/login")


class Register(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration.html"


def home(request):
    book = books.objects.all()
    return render(request, 'home.html',{'book':book})

def store(request):
    s = books()
    s.name = request.POST.get('name')
    s.author = request.POST.get('author')
    s.edition = request.POST.get('edition')
    s.publisher = request.POST.get('publisher')
    s.description = request.POST.get('description')
    s.save()
    return redirect('/home')

def addBooks(request):
    return render(request, 'addBooks.html')

def deletebook(request, pk):
    s = books.objects.get(id=pk)
    s.delete()
    messages.success(request, "Book deleted Successfully")
    return redirect('/home')

def updateView (request,pk):
    book = books.objects.get(id=pk)
    return render(request,'updatebook.html',{'book': book})


def update (request,pk):
    book = books.objects.get(id=pk)
    book.name = request.POST.get('name')
    book.author = request.POST.get('author')
    book.edition = request.POST.get('edition')
    book.publisher = request.POST.get('publisher')
    book.description = request.POST.get('description')
    book.save()
    messages.success(request, "Book Updated Successfully")
    return redirect('/home')


def search(request):
    searched = request.GET['searched']
    if len(searched) > 20:
        booklist = books.objects.none()
    else:
        booklistname = books.objects.filter(name__icontains=searched)
        booklistauth = books.objects.filter(author__icontains=searched)
        booklist = booklistname.union(booklistauth)

    if booklist.count() == 0:
        messages.warning(request,"No search result found. Please search it again")

    return render(request, 'search.html',{'booklist': booklist, 'searched': searched})


#serializer
def book_list(request):
    book = books.objects.all()
    serializer = Bookserializer(book, many=True)
    return JsonResponse(serializer.data, safe=False)
