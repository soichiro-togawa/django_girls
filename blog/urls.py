#Djangoの path 関数と、blog アプリの全てのビューをインポート
from django.urls import path
from . import views

#url、view、urlの名前(好きなもの)、の順番
urlpatterns = [
    path('', views.post_list, name='post_list'),
]