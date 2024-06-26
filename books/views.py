
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer