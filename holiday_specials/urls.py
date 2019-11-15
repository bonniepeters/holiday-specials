from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('shows', views.ShowList.as_view(), name='show_list'),
    path('show/add', views.ShowCreate.as_view(), name='show_create'),
    path('shows/<int:pk>', views.ShowDetail.as_view(), name='show_detail'),
    path('episodes', views.EpisodeList.as_view(), name='episode_list'),
    path('episodes/<int:pk>', views.EpisodeDetail.as_view(), name='episode_detail'),
]