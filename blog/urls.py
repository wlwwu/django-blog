from django.urls import path
from . import views

app_name = "blog"  #new added line after changing myside/url.py path from commentted to new
urlpatterns = [
    path('', views.blog_title, name='blog_title'),
    path('<int:article_id>', views.blog_article,name='blog_article'),
]