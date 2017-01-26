# -*- coding: utf-8 -*- 
from .models import Charger
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core import serializers
import requests
import string
import json

def Chargerlistup(request):
    chargerURL="http://ev.or.kr/portal/monitor/chargerList"
    charger_crawl = requests.get(chargerURL)   
    chargers_data = charger_crawl.text
    chargers_json = json.loads(chargers_data)
    for charger_data in chargers_json['chargerList']:
        try:
            Charger.objects.filter(statId=charger_data['sid'])
        except:
            hash_charger = Charger(statId=charger_data['sid'], statNm = charger_data['snm'], chgerId = charger_data['cid'], chgerType = charger_data['ctp'], stat=charger_data['cst'], addrDoro=charger_data['dro'], lat=charger_data['x'], lng=charger_data['y'], useTime=charger_data['utime'], LastUsedTime="09:00")
            hash_charger.save()
    return HttpResponse("up")


def Chargerlist(request):
    data = serializers.serialize("json", Charger.objects.all())
    return HttpResponse(data, content_type='json')