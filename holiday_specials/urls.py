from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('shows/<int:pk>', views.show_detail, name='show_detail'),
    path('episodes', views.episode_list, name='episode_list'),
    path('episodes/<int:pk>', views.episode_detail, name='episode_detail'),
    path('show/new', views.show_create, name='show_create'),
    path('episode/new', views.episode_create, name='episode_create'),
]