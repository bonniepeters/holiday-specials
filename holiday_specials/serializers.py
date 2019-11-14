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

    # def create(self, validated_data):
    #     episode = Episode.objects.create(show=validated_data['show']['id'],
    #         name=validated_data['name'], 
    #         description=validated_data['description'], 
    #         season=validated_data['season'],
    #         episode=validated_data['episode'],
    #         date=validated_data['date'],)
    #     return episode