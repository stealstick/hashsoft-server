import os
from django.db import models
from django.dispatch import receiver
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from .models import User
from .serializers import UserSerializer, PasswordSerializer, UserUpdateSerializer
from .permissions import IsOwnerOrReadOnly

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


    @detail_route(methods=['PUT'])
    def set_password(self, request, pk=None):
        serializer = PasswordSerializer(self.request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)


@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    try:
        old_file = User.objects.get(pk=instance.pk).profile.path
    except User.DoesNotExist:
        return False


    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).profile
    except User.DoesNotExist:
        return False

    new_file = instance.profile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



def test(request):
    return render(request, 'accounts/test.html')
