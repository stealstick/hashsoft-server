
from django.core.management.base import BaseCommand, CommandError
from chargers.models import Charger
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.core import serializers
import requests
import string
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        # -*- coding: utf-8 -*- 
        chargerURL="http://ev.or.kr/portal/monitor/chargerList"
        charger_crawl = requests.get(chargerURL)   
        chargers_data = charger_crawl.text
        chargers_json = json.loads(chargers_data)
        for charger_data in chargers_json['chargerList']:
            try:
                print(charger_data['sid'])
                print(charger_data['snm'])
                print(charger_data['cid'])
                print(charger_data['ctp'])
                print(charger_data['cst'])
                print(charger_data['dro'])
                print(charger_data['x'])
                print(charger_data['y'])
                print(charger_data['utime'])
                hash_charger = Charger.objects.create(unique_id=charger_data['sid']+charger_data['cid'], sid=charger_data['sid'], name = charger_data['snm'], cid = charger_data['cid'], ctype = charger_data['ctp'], stat=charger_data['cst'], addrDoro=charger_data['dro'], lat=charger_data['x'], lng=charger_data['y'], useTime=charger_data['utime'], LastUsedTime="09:00", bid=charger_data['chgeMange'])
            except:
                hash_ch=Charger.objects.get(unique_id=charger_data['sid']+charger_data['cid'])
                hash_ch.name = charger_data['snm']
                try:
                    hash_ch.bid=charger_data['chgeMange']
                except:
                    hash_ch.bid=10
                hash_ch.stat=charger_data['cst']
                hash_ch.addrDoro= charger_data['dro']
                hash_ch.lat=charger_data['x']
                hash_ch.lng=charger_data['y']
                hash_ch.useTime=charger_data['utime']
                if hash_ch.stat==3:
                    hash_ch.LastUsedTime=str(datetime.now())
                hash_ch.save()