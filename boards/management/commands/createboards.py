from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup

from boards.models import Board


class Command(BaseCommand):

    def handle(self, *args, **options):
        board_url = "http://ev.or.kr/portal/board/8/"
        for x in range(1, 1500):
            board_id = str(x)
            board_req = board_url + board_id
            r = requests.get(board_req)
            if r.text.count('충전인프라 정보시스템 에러 내용'):
                pass
            else:
                soup = BeautifulSoup(r.text, 'html.parser')

                for data in soup.find_all('em'):
                    data_str = str(data.get_text())
                    if data_str.count('-'):
                        board_date = data_str

                    elif data_str.isdigit():
                        board_count = data_str
                    else:
                        board_writer = data_str

                board_cont = soup.find("div", {"class": "view_cont"})
                board_cont = str(board_cont.get_text())
                board_title = soup.find("h3")
                board_title = str(board_title.get_text())
                try:
                    hash_board = Board.objects.create(
                        title=board_title, writer=board_writer,
                        content=board_cont, date=board_date)
                except:
                    hash_board = Board.objects.get(title=board_title)
                    hash_board.writer = board_writer
                    hash_board.content = board_cont
                    hash_board.date = board_date
                    hash_board.save()
