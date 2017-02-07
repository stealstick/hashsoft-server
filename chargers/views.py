import json

from django.http import HttpResponse
from django.core import serializers

import requests

from rest_framework import viewsets
from .serializers import ChargerSerializer
from .models import Charger


class ChargerViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()


def Chargerlistup(request):
    chargerURL="http://ev.or.kr/portal/monitor/chargerList"
    charger_crawl = requests.get(chargerURL)   
    chargers_data = charger_crawl.text
    chargers_json = json.loads(chargers_data)
    for charger_data in chargers_json['chargerList']:
        try:
            hash_charger = Charger.objects.create(statId=charger_data['sid'], statNm = charger_data['snm'], chgerId = charger_data['cid'], chgerType = charger_data['ctp'], stat=charger_data['cst'], addrDoro=charger_data['dro'], lat=charger_data['x'], lng=charger_data['y'], useTime=charger_data['utime'], LastUsedTime="09:00")
        except:
            hash_ch=Charger.objects.get(statId=charger_data['sid'])
            hash_ch.statNm = charger_data['snm']
            hash_ch.chgerId = charger_data['cid']
            hash_ch.chgerType = charger_data['ctp']
            hash_ch.stat=charger_data['cst']
            hash_ch.addrDoro= charger_data['dro']
            hash_ch.lat=charger_data['x']
            hash_ch.lng=charger_data['y']
            hash_ch.useTime=charger_data['utime']
            hash_ch.save()
    return HttpResponse("up")


def Chargerlist(request):
    data = serializers.serialize("json", Charger.objects.all())
    return HttpResponse(data, content_type='json')


