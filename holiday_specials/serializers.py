from rest_framework import serializers
from .models import Show, Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'show', 'Title', 'Released', 'Season', 'Episode', 'Runtime', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'imdbSeriesID', 'justWatchUrl',)

class ShowSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Show
        fields = ('id', 'Title', 'Year', 'Genre', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'totalSeasons', 'justWatchUrl', 'episodes',)