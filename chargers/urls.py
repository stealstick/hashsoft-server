from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^chargerlist$', views.Chargerlist),
	url(r'^chargerlistup$', views.Chargerlistup),
]