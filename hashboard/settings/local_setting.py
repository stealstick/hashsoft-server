from hashboard.settings.base import *  # NOQA

# HTTP 호스트 헤더  변조를 이용한 공격에 보안상 이유로 허용 하는 호스트 설정
# '*'로 설정시 모든 호스트를, 'localhost' or '127.0.0.1'로 설정시 로컬에서만 접속이 가능 하게 함
# https://docs.djangoproject.com/en/1.10/ref/settings/
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
