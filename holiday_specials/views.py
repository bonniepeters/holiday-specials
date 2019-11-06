from django.shortcuts import render
from .models import Show, Episode

def show_list(request):
    shows = Show.objects.all()
    return render(request, 'holiday_specials/show_list.html', {'shows': shows})

def show_detail(request, pk):
    show = Show.objects.all()
    return render(request, 'holiday_specials/show_detail.html', {'show': show})

def episode_list(request):
    episodes = Episode.objects.all()
    return render(request, 'holiday_specials/episode_list.html', {'episodes': episodes})

def episode_detail(request, pk):
    episode = Episode.objects.all()
    return render(request, 'holiday_specials/episode_detail.html', {'episode': episode})