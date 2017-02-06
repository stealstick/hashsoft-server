from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from .models import User, UserCarType
from .serializers import UserSerializer, PasswordSerializer, UserCarTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = (MultiPartParser, FormParser,)

    def update(self, request, pk=None):
        # TODO UserSerializer에서 update로 바꾸기
        user = User.objects.get(pk=pk)
        user.username = request.data.get('username', user.username)
        user.sex = request.data.get('sex', user.sex)
        user.place = request.data.get('place', user.place)
        user.year = request.data.get('year', user.year)
        user.profile = request.FILES.get('profile', user.profile)
        user.save()
        return Response(user)


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
