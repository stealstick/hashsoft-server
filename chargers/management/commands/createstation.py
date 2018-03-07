
from django.core.management.base import BaseCommand, CommandError
from chargers.models import Charger, CidStat
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
                print(charger_data['chgeMange'])
                if charger_data['chgeMange']   == "11" or charger_data['chgeMange']   == 11:
                    charger_data['chgeMange'] = 'BG'
                elif charger_data['chgeMange']   == "12" or charger_data['chgeMange']   == 12:
                    charger_data['chgeMange'] = 'JE'
                elif charger_data['chgeMange']   == "13" or charger_data['chgeMange']   == 13:
                    charger_data['chgeMange'] = 'KP'
                elif charger_data['chgeMange']   == "14" or charger_data['chgeMange']   == 14:
                    charger_data['chgeMange'] = 'HE'
                elif charger_data['chgeMange']   == "15" or charger_data['chgeMange']   == 15:
                    charger_data['chgeMange'] = 'PI'
                elif charger_data['chgeMange']   == "16" or charger_data['chgeMange']   == 16:
                    charger_data['chgeMange'] = 'SE'
                elif  charger_data['chgeMange']   == "17" or charger_data['chgeMange']   == 17:
                    charger_data['chgeMange'] = 'GI'
                elif  charger_data['chgeMange']   == "18" or charger_data['chgeMange']   == 18:
                    charger_data['chgeMange'] = 'HD'
                elif  charger_data['chgeMange']   == "19" or charger_data['chgeMange']   == 19:
                    charger_data['chgeMange'] = 'JD'
                elif  charger_data['chgeMange']   == "20" or charger_data['chgeMange']   == 20:
                    charger_data['chgeMange'] = 'DG'
                elif  charger_data['chgeMange']   == "22" or charger_data['chgeMange']   == 22:
                    charger_data['chgeMange'] = 'SS'
                elif  charger_data['chgeMange']   == "23" or charger_data['chgeMange']   == 23:
                    charger_data['chgeMange'] = 'ST'
                elif  charger_data['chgeMange']   == "24" or charger_data['chgeMange']   == 24:
                    charger_data['chgeMange'] = 'GN'
                elif  charger_data['chgeMange']   == "25" or charger_data['chgeMange']   == 25:
                    charger_data['chgeMange'] = 'KT'
                elif  charger_data['chgeMange']   == "26" or charger_data['chgeMange']   == 26:
                    charger_data['chgeMange'] = 'ER'
                elif  charger_data['chgeMange']   == "27" or charger_data['chgeMange']   == 27:
                    charger_data['chgeMange'] = 'WR1'
                elif  charger_data['chgeMange']   == "28" or charger_data['chgeMange']   == 28:
                    charger_data['chgeMange'] = 'WR2'
                elif  charger_data['chgeMange']   == "29" or charger_data['chgeMange']   == 29:
                    charger_data['chgeMange'] = 'WR3'
                elif  charger_data['chgeMange']   == "30" or charger_data['chgeMange']   == 30:
                    charger_data['chgeMange'] = 'WR4'
                elif  charger_data['chgeMange']   == "89" or charger_data['chgeMange']   == 89: 
                    charger_data['chgeMange'] = 'HO'
                elif  charger_data['chgeMange']   == "" or charger_data['chgeMange']   == None: 
                    charger_data['chgeMange'] = 'ME'
                else:
                    charger_data['chgeMange'] = 'None'
                if charger_data['cst'] is 7:
                    charger_data['chgeMange'] = 'MT'
                    charger_data['cst'] = charger_data['tst']

                print(charger_data['sid'])
                print(charger_data['chgeMange'])

                hash_charger = Charger.objects.create(sid=charger_data['sid'], name = charger_data['snm'], ctype = charger_data['ctp'], addrDoro=charger_data['adr'], lat=charger_data['x'], lng=charger_data['y'], useTime=charger_data['utime'], LastUsedTime="09:00", bid=charger_data['chgeMange'])
            except:
                hash_ch=Charger.objects.get(sid=charger_data['sid'])
                hash_ch.name = charger_data['snm']
                try:
                    hash_ch.bid=charger_data['chgeMange']
                except:
                    hash_ch.bid=10
                hash_ch.stat=charger_data['cst']
                hash_ch.addrDoro= charger_data['adr']
                hash_ch.lat=charger_data['x']
                hash_ch.lng=charger_data['y']
                hash_ch.useTime=charger_data['utime']
                hash_ch.save()
