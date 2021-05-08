from django.shortcuts import render
from django.http import HttpResponse
from.models import Book


# Create your views here.
def home(request):

    book=Book.objects.all()
    return render(request, "index.html",{"book":book})
