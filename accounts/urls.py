from django.conf.urls import url
from . import views

urlpatterns = [
    url('^test/$', views.test, name="test"),
    url('^token/$', views.ObtainAuthToken.as_view(), name="token"),
]