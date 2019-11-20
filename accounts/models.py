from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# user model 커스터마이징
class User(AbstractUser):
    followers = models.ManyToManyField(  # 유저에게는 follower라는 필드가 있다, 내가 여러 명 팔로워 가능, 팔로잉 가능(모델끼리)
        settings.AUTH_USER_MODEL,
        related_name='followings'  # 팔로잉하는 사람들 가져오기 user.followings
    )


