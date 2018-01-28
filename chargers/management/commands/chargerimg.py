from django.core.management.base import BaseCommand
from chargers.models import Charger
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import urlopen
from django.core.files.base import ContentFile

class Command(BaseCommand):

    def handle(self, *args, **options):
        # -*- coding: utf-8 -*- 
        queryset=Charger.objects.all()
        for charger in queryset:
            chargerURL="http://ev.or.kr/portal/monitor/stationinfo?sid="+charger.sid
            charger_crawl=requests.get(chargerURL)
            charger_html=charger_crawl.text
            soup = BeautifulSoup(charger_html, 'html.parser')
            pic=soup.find_all(alt="충전소 사진")
            try:
                img_locate=str(pic[0]['src'])
                img_url="http://ev.or.kr" + img_locate
                img01=urlopen(img_url)
                charger.charger_img1.save('a.jpg', ContentFile(img01.read()))
                charger.save()
                print("success")

                img_locate=str(pic[1]['src'])
                img_url="http://ev.or.kr"+img_locate
                img02=urlopen(img_url)
                charger.charger_img2.save('a.jpg', ContentFile(img02.read()))
                charger.save()
                print("success2")
            except:
                pass
