from rest_framework import serializers
from .models import Show, Episode

class ShowSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Show
        fields = ('id', 'Title', 'Year', 'Genre', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'totalSeasons', 'justWatchUrl', 'episodes',)

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'show', 'Title', 'Released', 'Season', 'Episode', 'Runtime', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'imdbSeriesID', 'justWatchUrl',)
        
    # def create(self, validated_data):
    #     episode = Episode.objects.create(show=validated_data['show']['id'],
    #         Title=validated_data['Title'], 
    #         Released=validated_data['Released'], 
    #         Season=validated_data['Season'],
    #         Episode=validated_data['Episode'],
    #         Runtime=validated_data['Runtime'],
    #         Plot=validated_data['Plot'],
    #         Poster=validated_data['Poster'],
    #         imdbRating=validated_data['imdbRating'],
    #         imdbVotes=validated_data['imdbVotes'],
    #         imdbID=validated_data['imdbID'],
    #         imdbSeriesID=validated_data['imdbSeriesID'],
    #         justWatchUrl=validated_data['justWatchUrl'],)
    #     return episode

    # def update(self, instance, validated_data):
    #     instance.show = validated_data.get(('show')('id'), instance.show)
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.Title = validated_data.get('Title', instance.Title) 
    #     instance.Released = validated_data.get('Released', instance.Released)
    #     instance.Season = validated_data.get('Season', instance.Season)
    #     instance.Episode = validated_data.get('Episode', instance.Episode)
    #     instance.Runtime = validated_data.get('Runtime', instance.Runtime)
    #     instance.Plot = validated_data.get('Plot', instance.Plot)
    #     instance.Poster = validated_data.get('Poster', instance.Poster)
    #     instance.imdbRating = validated_data.get('imdbRating', instance.imdbRating)
    #     instance.imdbVotes = validated_data.get('imdbVotes', instance.imdbVotes)
    #     instance.imdbID = validated_data.get('imdbID', instance.imdbID)
    #     instance.imdbSeriesID = validated_data.get('imdbSeriesID', instance.imdbSeriesID)
    #     instance.justWatchUrl = validated_data.get('justWatchUrl', instance.justWatchUrl)
    #     instance.save()
    #     return instance
