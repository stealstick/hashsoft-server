
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

                        if (charger_data['cid']   == "11" || charger_data['cid']   == 11 ):
                                charger_data['cid'] = 'BG'
                        elif charger_data['cid']   == "12" || charger_data['cid']   == 12:
                                charger_data['cid'] = 'JE'
                        elif charger_data['cid']   == "13" || charger_data['cid']   == 13:
                                charger_data['cid'] = 'KP'
                        elif charger_data['cid']   == "14" || charger_data['cid']   == 14:
                                charger_data['cid'] = 'HE'
                        elif charger_data['cid']   == "15" || charger_data['cid']   == 15:
                                charger_data['cid'] = 'PI'
                        elif charger_data['cid']   == "16" || charger_data['cid']   == 16:
                                charger_data['cid'] = 'SE'
                        elif  charger_data['cid']   == "17" || charger_data['cid']   == 17:
                                charger_data['cid'] = 'GI'
                        elif  charger_data['cid']   == "18" || charger_data['cid']   == 18:
                                charger_data['cid'] = 'HD'
                        elif  charger_data['cid']   == "19" || charger_data['cid']   == 19:
                                charger_data['cid'] = 'JD'
                        elif  charger_data['cid']   == "20" || charger_data['cid']   == 20:
                                charger_data['cid'] = 'DG'
                        elif  charger_data['cid']   == "22" || charger_data['cid']   == 22:
                                charger_data['cid'] = 'SS'
                        elif  charger_data['cid']   == "23" || charger_data['cid']   == 23:
                                charger_data['cid'] = 'ST'
                        elif  charger_data['cid']   == "24" || charger_data['cid']   == 24:
                                charger_data['cid'] = 'GN'
                        elif  charger_data['cid']   == "25" || charger_data['cid']   == 25:
                                charger_data['cid'] = 'KT'
                        elif  charger_data['cid']   == "26" || charger_data['cid']   == 26:
                                charger_data['cid'] = 'EV'
                        elif  charger_data['cid']   == "27" || charger_data['cid']   == 27:
                                charger_data['cid'] = 'WR1'
                        elif  charger_data['cid']   == "28" || charger_data['cid']   == 28:
                                charger_data['cid'] = 'WR2'
                        elif  charger_data['cid']   == "29" || charger_data['cid']   == 29:
                                charger_data['cid'] = 'WR3'
                        elif  charger_data['cid']   == "30" || charger_data['cid']   == 30:
                                charger_data['cid'] = 'WR4'
                        elif  charger_data['cid']   == "89" || charger_data['cid']   == 89: 
                                charger_data['cid'] = 'HO'
                        else
                                charger_data['cid'] = 'ME'
                                
                                if charger_data['cst'] is 7:
                                        charger_data['cid'] = 'ME_T'
                                        charger_data['tst']




                        print(charger_data['ctp'])
                        print(charger_data['cst'])
                        print(charger_data['dro'])
                        print(charger_data['x'])
                        print(charger_data['y'])
                        print(charger_data['utime'])
                        hash_charger = Charger.objects.create(unique_id=charger_data['sid']+charger_data['cid'], sid=charger_data['sid'], name = charger_data['snm'], cid = charger_data['cid'], ctype = charger_data['ctp'], stat=charger_data['cst'], addrDoro=charger_data['dro'], lat=charger_data['x'], lng=charger_data['y'], useTime=charger_data['utime'], LastUsedTime="09:00", bid=charger_data['charger_data['cid']  '])
                except:
                        hash_ch=Charger.objects.get(unique_id=charger_data['sid']+charger_data['cid'])
                        hash_ch.name = charger_data['snm']
                        try:
                                hash_ch.bid=charger_data['charger_data['cid']  ']
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