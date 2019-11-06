from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('shows/<int:pk>', views.show_detail, name='show_detail'),
    path('episodes', views.episode_list, name='episode_list'),
    path('episodes/<int:pk>', views.episode_detail, name='episode_detail'),
]