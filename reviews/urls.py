from django.conf.urls import url
from .views import statId_review

urlpatterns = [
    url(r'^statId_review/(?P<statId>[\w+-]*)$', statId_review, name="statId_review")
]