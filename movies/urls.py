from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movielist, name='index'),
    path('detail/<int:movie_pk>/', views.moviedetail, name='moviedetail'),
    path('<int:movie_pk>/reviews_create', views.reviews_create, name='create'),
    path('<int:movie_pk>/reviews_delete/<int:review_pk>', views.reviews_delete, name='delete'),
    path('<int:movie_pk>/like', views.like, name='like'),
]
