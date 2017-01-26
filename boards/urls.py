from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^notice$', views.Notice),
    url(r'^noticeup$', views.Noticeup),
]