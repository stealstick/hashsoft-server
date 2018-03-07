
from django.core.management.base import BaseCommand, CommandError
from chargers.models import CidStat, Charger
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

            station=Charger.objects.get(sid=charger_data['sid'])
            try:
                if charger_data['cst'] is 7:
                    charger_data['chgeMange'] = 'MT'
                    charger_data['cst'] = charger_data['tst']

                """
                print(charger_data['sid'])
                print(charger_data['chgeMange'])
                print(charger_data['snm'])
                print(charger_data['cid'])
                print(charger_data['ctp'])
                print(charger_data['cst'])
                print(charger_data['adr'])
                print(charger_data['x'])
                print(charger_data['y'])
                print(charger_data['utime'])
                """

                hash_charger = Charger.objects.crete(sidcid=charger_data['sid']+charger_data['cid'], cid=charger_data['cid'], stat=int(charger_data['cst']),sid=station, ctype=charger_data['ctp'])
            except:
                print(charger_data['sid']+charger_data['cid'])
                try:
                    hash_ch=CidStat.objects.get(sidcid=charger_data['sid']+charger_data['cid'])
                    hash_ch.stat=charger_data['cst']
                    hash_ch.ctype=charger_data['ctp']
                    hash_ch.save()
                
                except:
                    pass
                

                print(hash_ch.sidcid)
