# -*- coding: utf-8 -*- 
from .models import board
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from bs4 import BeautifulSoup
from django.core import serializers
import requests
import string

def noticeup(request):
    board_url="http://ev.or.kr/portal/board/8/"
    for x in range(1,1500):
        board_id=str(x)
        board_req = board_url+board_id
        r = requests.get(board_req)
        if r.text.count('충전인프라 정보시스템 에러 내용'):
            pass
        else:
            #print (r.text)
            soup = BeautifulSoup(r.text)
            
            for data in soup.find_all('em'):
                data_str=str(data.get_text())
                if data_str.count('-'):
                    board_date = data_str

                elif data_str.isdigit():
                    board_count = data_str
                else:
                    board_writer = data_str
                    
            board_cont=soup.find("div", {"class" : "view_cont"})
            board_cont=str(board_cont.get_text())
            board_title=soup.find("h3")
            board_title=str(board_title.get_text())
            hash_board = board(title=board_title, writer = board_writer, content = board_cont, date = board_date)
            hash_board.save()
            
    return HttpResponse("done")

def notice(request):
    
    hashboard = board.objects.all()
    hashboard = list(hashboard)
    data = serializers.serialize("json", board.objects.all())
    return HttpResponse(data, content_type='json')