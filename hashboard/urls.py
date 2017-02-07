"""hashboard URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

from accounts.views import UserViewSet, UserCarTypeViewSet
from chargers.views import ChargerViewSet
from boards.views import BoardViewSet
from reviews.views import ChargerReviewViewSet



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chargers', ChargerViewSet)
router.register(r'usercartypes', UserCarTypeViewSet, base_name="usercartype")
router.register(r'boards', BoardViewSet, base_name="board")
router.register(r'charger_reviews', ChargerReviewViewSet, base_name="charger_review")


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls, namespace="rest")),
    url(r'^auth/login/', token_views.obtain_auth_token),

    url(r'^accounts/', include('accounts.urls', namespace="accounts")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
