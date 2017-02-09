from django.core.management.base import BaseCommand
from chargers.models import Charger
from bs4 import BeautifulSoup
import requests
import urllib.request


class Command(BaseCommand):

    def handle(self, *args, **options):
        # -*- coding: utf-8 -*- 
        queryset = Charger.objects.all()
        for charger in queryset:
            chargerURL="http://ev.or.kr/portal/monitor/stationinfo?sid="+charger.statId
            charger_crawl = requests.get(chargerURL)   
            charger_html = charger_crawl.text
            soup = BeautifulSoup(charger_html, 'html.parser')
            pic=soup.find_all(alt="충전소 사진")
            try:
                img_locate=str(pic[0]['src'])
                img_url="http://ev.or.kr"+img_locate
                urllib.request.urlretrieve(img_url, "media/"+charger.statId+"_1.png")
                charger_get=Charger.objects.get(statId=charger.statId)
                charger_get.charger_img1=charger.statId+"_1.png"
                charger_get.save()

                img_locate=str(pic[1]['src'])
                img_url="http://ev.or.kr"+img_locate
                urllib.request.urlretrieve(img_url, "media/"+charger.statId+"_2.png")
                charger_get=Charger.objects.get(statId=charger.statId)
                charger_get.charger_img2=charger.statId+"_2.png"
                charger_get.save()
            except:
                pass
