from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^api$', views.index),
    url(r'^board$', views.all),
]