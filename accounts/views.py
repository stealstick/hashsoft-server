from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import status

from .models import User
from .serializers import UserSerializer, PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, pk=None):
        # TODO Testing 후 request.user로 고치기
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
            user = serializer.save(**serializer.validated_data)
            user.set_password(user.password)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['PUT'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


def test(request):
    return render(request, 'accounts/test.html')