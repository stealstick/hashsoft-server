from django.core.management.base import BaseCommand
import time
import requests
from bs4 import BeautifulSoup

from boards.models import Board, Dataroom


class Command(BaseCommand):

    def handle(self, *args, **options):
        board_url = "http://ev.or.kr/portal/board/9/"
        for x in range(210, 3500):
            board_id = str(x)
            board_req = board_url + board_id
            print(x)
            try:
                r = requests.get(board_req)
            except:
                time.sleep(3)
                r = requests.get(board_req)
            if r.text.count('잘못된 주소이거나') or r.text.count('충전인프라 정보시스템 에러'):
                pass
            else:
                print(board_req)
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
                board_context = str(board_cont.get_text())
                board_title = soup.find("h3")
                board_title = str(board_title.get_text())
                try:
                    board_filelink = board_cont.find_all('a', href=True)
                    board_filelink=str(board_filelink['href'])
                    board_filelink="http://ev.or.kr"+board_filelink[0]
                    print(x)
                except:
                    board_filelink="none"


                try:
                    hash_board = Dataroom.objects.create(
                        title=board_title, writer=board_writer,
                        content=board_context, date=board_date, filelink=board_filelink)
                except:
                    hash_board = Dataroom.objects.get(title=board_title)
                    hash_board.writer = board_writer
                    hash_board.content = board_context
                    hash_board.date = board_date
                    hash_board.filelink = board_filelink
                    hash_board.save()
