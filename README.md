```shell
from django_resized import ResizedImageField
```
- pip install Pillow
-> Python Imaging Library(PIL)의 확장된 버전으로, 이미지를 처리하는 데 필요
- pip install django-resized
-> 이미지를 리사이즈하는 Django 패키지

## accounts 
- django.contrib.auth.models.AbstractUser
Django의 기본 User 모델을 확장할 수 있도록 제공되는 클래스
Django에서는 기본적으로 User 모델을 제공하는데, AbstractUser를 사용하면 이 기본 User 모델을 커스텀할 수 있음

- ResizedImageField
ResizedImageField는 이미지 크기를 자동으로 조절하는 필드

기본적으로 Django는 ImageField를 제공하지만, 이미지를 업로드할 때 크기를 줄이는 기능이 없어.

ResizedImageField를 사용하면 업로드된 이미지를 특정 크기로 자동 리사이징

- AUTH_USER_MODEL = 'accounts.User' # 내가 직접 만든 커스텀 User 모델을 사용할 거야
-> 모델을 만들고 처음 마이그레이션 하기 전에 설정

- __init__.py는 그 폴더가 "파이썬 패키지(package)"라는 걸 알려주는 파일. 즉, migrations 폴더에 __init__.py가 있어야만
Django가 이 폴더를 정상적인 마이그레이션 모듈로 인식할 수 있음

- python manage.py makemigrations -> 마이그레이션 파일 생성
- python manage.py migrate -> DB에 적용
