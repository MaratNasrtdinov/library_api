from rest_framework import serializers


class BookListSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=128)
    author = serializers.CharField(max_length=64)
    year = serializers.IntegerField()
    ISBN = serializers.CharField(max_length=20)