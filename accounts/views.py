from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken import views as rest_view
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer
from .forms import UserCreateForm

class ObtainAuthToken(rest_view.ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        context = {
            'token': token.key,
            'pk': str(user.pk),
            'username': user.username,
            'profilePath': user.profile.url,
        }
        return Response(context)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        forms = UserCreateForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        return Response({"Fail":"user create fail"})



def test(request):
    context = {
        'UserCreateForm' : UserCreateForm
    }
    return render(request, 'accounts/test.html', context)