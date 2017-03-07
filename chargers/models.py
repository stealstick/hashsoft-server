from django.db import models

# Create your models here.


class Charger(models.Model):
    no=10
    BG=11
    JR=12
    KP=13
    KC=14
    PI=15
    SC=16
    KI=17
    HD=18
    JE=19
    DA=20
    SU=89
    CHARGER_COM = (
        (no, 'none'),
        (BG, '비긴스'),
        (JR, '제주전기자동차서비스'),
        (KP, '한국전력'),
        (KC, '한국전기차충전서비스'),
        (PI, '포스코ICT'),
        (SC, '서울시한국자동차환경협회'),
        (KI, '기아자동차'),
        (HD, '현대자동차'),
        (JE, '제주특별자치도청'),
        (DA, '대구환경공단'),
        (SU, '수소충전소')
    )
    statId = models.CharField(max_length=100, help_text="충전소 아이디", unique=True)
    statNm = models.CharField(max_length=100, help_text="충전소 이름")
    chgerId = models.PositiveIntegerField(default=0, help_text="충전기 아이디")
    chgerType = models.PositiveIntegerField(default=0, help_text="충전기 타입")
    stat = models.PositiveIntegerField(default=0, help_text="실시간 정보")
    addrDoro = models.CharField(max_length=100, help_text="도로명")
    lat = models.FloatField(default=0, help_text="위도")
    lng = models.FloatField(default=0, help_text="경도")
    useTime = models.CharField(max_length=100, help_text="사용 가능 시간")
    LastUsedTime = models.CharField(max_length=20, help_text="마지막 사용 시간")
    Charger_Com=models.PositiveIntegerField(choices=CHARGER_COM, default=no, blank=False)
    charger_img1= models.ImageField(upload_to="cha", default="defalutChargerImg.jpg")
    charger_img2= models.ImageField(upload_to="cha", default="defalutChargerImg.jpg")

    def __str__(self):
        return self.statNm