from django.shortcuts import render, redirect
from .models import Show, Episode
from .forms import ShowForm, EpisodeForm

def show_list(request):
    shows = Show.objects.all()
    return render(request, 'holiday_specials/show_list.html', {'shows': shows})

def show_detail(request, pk):
    show = Show.objects.get(id=pk)
    return render(request, 'holiday_specials/show_detail.html', {'show': show})

def episode_list(request):
    episodes = Episode.objects.all()
    return render(request, 'holiday_specials/episode_list.html', {'episodes': episodes})

def episode_detail(request, pk):
    episode = Episode.objects.get(id=pk)
    return render(request, 'holiday_specials/episode_detail.html', {'episode': episode})

def show_create(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = form.save()
            return redirect('show_detail', pk=show.pk)
    else:
        form = ShowForm()
    return render(request, 'holiday_specials/show_form.html', {'form': form})

def episode_create(request):
    if request.method == 'POST':
        form = EpisodeForm(request.POST)
        if form.is_valid():
            show = form.save()
            return redirect('episode_detail', pk=episode.pk)
    else:
        form = EpisodeForm()
    return render(request, 'holiday_specials/episode_form.html', {'form': form})

def show_edit(request, pk):
    show = Show.objects.get(id=pk)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save()
            return redirect('show_detail', pk=show.pk)
    else:
        form = ShowForm(instance=show)
    return render(request, 'holiday_specials/show_form.html', {'form': form})

def episode_edit(request, pk):
    episode = Episode.objects.get(id=pk)
    if request.method == 'POST':
        form = EpisodeForm(request.POST, instance=episode)
        if form.is_valid():
            episode = form.save()
            return redirect('episode_detail', pk=episode.pk)
    else:
        form = EpisodeForm(instance=episode)
    return render(request, 'holiday_specials/episode_form.html', {'form': form})

def show_delete(request, pk):
    Show.objects.get(id=pk).delete()
    return redirect('show_list')

def episode_delete(request, pk):
    Episode.objects.get(id=pk).delete()
    return redirect('show_list')