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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet, UserCardViewSet, WarninViewSet
from boards.views import BoardViewSet
from chargers.views import ChargerViewSet
from reviews.views import ChargerReviewViewSet
from reports.views import ReportViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-cards', UserCardViewSet, base_name="user_card")
router.register(r'chargers', ChargerViewSet)
router.register(r'boards', BoardViewSet, base_name="board")
router.register(r'charger_reviews', ChargerReviewViewSet, base_name="charger_review")
router.register(r'reports', ReportViewSet, base_name="report")
router.register(r'warnings', WarninViewSet, base_name="warning")


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace="rest")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
