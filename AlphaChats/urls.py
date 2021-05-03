from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_room', views.create_room, name='create_room'),
    path('room-<str:rn>', views.room),
    path('chatwork', views.chatwork),
    path('getchat', views.get_msg),

]
