#Djangoの path 関数と、blog アプリの全てのビューをインポート
from django.urls import path
from . import views

#url、view、urlの名前(好きなもの)、の順番
urlpatterns = [
    #記載されたviewをurlと紐づける
    path('', views.post_list, name='post_list'),
    #post/整数のurl
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]