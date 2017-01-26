
from django.contrib.auth.forms import UserCreationForm as django_UserCreationForm
from .models import User

class UserCreateForm(django_UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "profile", 'sex', 'place')