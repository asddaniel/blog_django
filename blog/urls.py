

from django.urls import path
from blog import views


urlpatterns = [
path('articles/', views.get_article, name='article.all'),
path('articles/add/', views.post_article)
]