from django.contrib import admin
from django.urls import path
from App import views
urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:id>',views.details,name='details'),
    path('search/',views.search,name='search'),
    path('add_team/',views.add_team,name='add_team'),
    path('add_player/',views.add_player,name='add_player'),
]


