from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^notice$', views.notice),
    url(r'^noticeup$', views.noticeup),
]