from rest_framework import viewsets

from main.models import BookModel
from main.serializers import BookListSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookListSerializer




