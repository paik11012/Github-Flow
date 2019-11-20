from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    # 중계모델은 다대다 관계에서만 설정 가능
    genres = models.ManyToManyField(Genre, related_name='movies')
    # 영화와 유저 간 m:n 좋아요
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_users')

class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    # 누가 어떤 영화에 댓글을 달았는지 알기 위해서
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    