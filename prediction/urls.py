from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('matches/', views.matches, name='matches'),
    path('prediction/', views.predictresult, name='prediction'),
    path('result/', views.result, name='result'),
    path('matchresult', views.matchresult, name='matchresult'),
    path('players/',views.players, name='players')
]