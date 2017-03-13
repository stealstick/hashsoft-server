from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, list_route
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import User, UserCard, Warnin
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from .serializers import (UserSerializer, PasswordSerializer,
                          UserUpdateSerializer, AuthTokenSerializer,
                          UserCardSerializer, UserCardUpdateSerializer,
                          WarningSerializer
                          )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (IsOwnerOrReadOnly,)


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

    @list_route(methods=['POST'])
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    @list_route(methods=['GET'])
    def logout(self, request):
        if not request.user.is_authenticated:
            print(request.user)
            return Response("Do not exits user")
        request.user.auth_token.delete()
        return Response("user token delete success")

    @detail_route(methods=['PUT'])
    def set_password(self, request, pk=None):
        serializer = PasswordSerializer(self.request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserCardViewSet(viewsets.ModelViewSet):
    serializer_class = UserCardSerializer
    queryset = UserCard.objects.all()
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin]

    def update(self, request, pk=None):
        serializer = UserCardUpdateSerializer(UserCard.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class WarninViewSet(viewsets.ModelViewSet):
    serializer_class = WarningSerializer
    queryset = Warnin.objects.all()

    @list_route(methods=["POST"], permission_classes=[IsAdminUser])
    def add_user(self, request):
        title = request.data.get("title", None)
        email = request.data.get("email", None)
        try:
            warin=Warnin.objects.get(title=title)
            user=User.objects.get(email=email)
        except Warnin.DoesNotExist:
            return Response({"status":"title does not exist"})
        except User.DoesNotExist:
            return Response({"status": "email does not exist"})
        warin.users.add(user)
        warin.save()
        serializer = WarningSerializer(warin)
        return Response(serializer.data)


def test(request):
    return render(request, 'accounts/test.html')
