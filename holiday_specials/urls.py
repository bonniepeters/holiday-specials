from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('shows/<int:pk>', views.show_detail, name='show_detail'),
    path('episodes', views.episode_list, name='episode_list'),
    path('episodes/<int:pk>', views.episode_detail, name='episode_detail'),
    path('show/new', views.show_create, name='show_create'),
    path('episode/new', views.episode_create, name='episode_create'),
    path('show/<int:pk>/edit', views.show_edit, name='show_edit'),
    path('episode/<int:pk>/edit', views.episode_edit, name='episode_edit'),
    path('show/<int:pk>/delete', views.show_delete, name='show_delete'),
    path('episode/<int:pk>/delete', views.episode_delete, name='episode_delete'),
]