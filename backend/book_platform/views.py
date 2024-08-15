from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .google_books_api import search_books
from .models import Book
from .serializers import BookSerializer

class BookSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        books = search_books(query)
        return Response(books)
    


class BookRecommendationView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save