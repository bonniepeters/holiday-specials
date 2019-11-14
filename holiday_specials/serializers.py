from rest_framework import serializers
from .models import Show, Episode

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    episodes = serializers.HyperlinkedRelatedField(
        view_name='episode_detail',
        many=True,
        read_only=True
    )
    show_url = serializers.ModelSerializer.serializer_url_field(
        view_name='show_detail'
    )
    class Meta:
        model = Show
        fields = ('id', 'Title', 'Year', 'Genre', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'totalSeasons', 'justWatchUrl', 'episodes', 'show_url',)

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    show = serializers.PrimaryKeyRelatedField(queryset=Show.objects.all(), source='show.id')
    class Meta:
        model = Episode
        fields = ('id', 'show', 'Title', 'Released', 'Season', 'Episode', 'Runtime', 'Plot', 'Poster', 'imdbRating', 'imdbVotes', 'imdbID', 'imdbSeriesID', 'justWatchUrl', 'show_id',)
        
    def create(self, validated_data):
        episode = Episode.objects.create(show=validated_data['show']['id'],
            Title=validated_data['Title'], 
            Released=validated_data['Released'], 
            Season=validated_data['Season'],
            Episode=validated_data['Episode'],
            Runtime=validated_data['Runtime'],
            Plot=validated_data['Plot'],
            Poster=validated_data['Poster'],
            imdbRating=validated_data['imdbRating'],
            imdbVotes=validated_data['imdbVotes'],
            imdbID=validated_data['imdbID'],
            imdbSeriesID=validated_data['imdbSeriesID'],
            justWatchUrl=validated_data['justWatchUrl'],)
        return episode

    def update(self, validated_data):
        episode = Episode.objects.update(show=validated_data['show']['id'],
            Title=validated_data['Title'], 
            Released=validated_data['Released'], 
            Season=validated_data['Season'],
            Episode=validated_data['Episode'],
            Runtime=validated_data['Runtime'],
            Plot=validated_data['Plot'],
            Poster=validated_data['Poster'],
            imdbRating=validated_data['imdbRating'],
            imdbVotes=validated_data['imdbVotes'],
            imdbID=validated_data['imdbID'],
            imdbSeriesID=validated_data['imdbSeriesID'],
            justWatchUrl=validated_data['justWatchUrl'],)
        return episode
