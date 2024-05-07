from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializers):

    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn", "price",)