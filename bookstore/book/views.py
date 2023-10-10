from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


# ModelViewSet includes implementations for CRUD Operations
# It provides .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
