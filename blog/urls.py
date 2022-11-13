

from django.urls import path
from blog import views


urlpatterns = [
path('articles/', views.get_article, name='article.all'),
path('add/', views.post_article, name='article.add')
]