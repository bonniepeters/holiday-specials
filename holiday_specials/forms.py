from django import forms
from .models import Show, Episode

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('name', 'description', 'streaming_on', 'image_url', 'imdb_url', 'genre',)

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ('show', 'name', 'description', 'season', 'episode', 'date',)