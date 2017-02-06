from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from .models import User, UserCarType
from .serializers import UserSerializer, PasswordSerializer, UserCarTypeSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = (MultiPartParser, FormParser,)

    def update(self, request, pk=None):
        serializer = UserUpdateSerializer(self.request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    @detail_route(methods=['PUT', 'POST'])
    def set_password(self, request, pk=None):
        serializer = PasswordSerializer(self.request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(self.request.user.password)
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserCarTypeViewSet(viewsets.ModelViewSet):
    serializer_class = UserCarTypeSerializer
    queryset = UserCarType.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def test(request):
    return render(request, 'accounts/test.html')
