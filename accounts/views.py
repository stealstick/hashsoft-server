from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(**serializer.validated_data)
        user.set_password(user.password)
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


def test(request):
    return render(request, 'accounts/test.html')