from django.shortcuts import render
from rest_framework import generics, serializers,permissions
from .models import Book
from .serializers import Bookserializere
from rest_framework.filters import SearchFilter

# Create your views here.
class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializere

    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializere
    
    
    