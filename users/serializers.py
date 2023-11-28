from rest_framework import serializers


class UserModelSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(max_length=64)
    email = serializers.EmailField(max_length=64)
