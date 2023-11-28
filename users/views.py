from rest_framework import generics

from users.models import UserModel
from users.serializers import UserModelSerializer


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
