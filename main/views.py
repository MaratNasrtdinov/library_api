from rest_framework import viewsets

from .models import BookModel
from .serializers import BookListSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookListSerializer




