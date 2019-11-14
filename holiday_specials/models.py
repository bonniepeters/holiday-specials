from django.db import models

class Show(models.Model):
    Title = models.CharField(max_length=60, default='')
    Year = models.CharField(max_length=10, default='')
    Genre = models.CharField(max_length=10, default='')
    Plot = models.TextField(default='')
    Poster = models.TextField(default='')
    imdbRating = models.DecimalField(default=5, max_digits=2, decimal_places=1)
    imdbVotes = models.CharField(max_length=30, default='')
    imdbID = models.CharField(max_length=15, default='')
    totalSeasons = models.PositiveIntegerField(default=1)
    justWatchUrl = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.Title

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='episodes')
    Title = models.CharField(max_length=100, default='')
    Released = models.CharField(max_length=15, default='')
    Season = models.PositiveIntegerField(default=1)
    Episode = models.PositiveIntegerField(default=10)
    Runtime = models.CharField(max_length=15, default='')
    Plot = models.TextField(default='')
    Poster = models.TextField(default='')
    imdbRating = models.DecimalField(default=5, max_digits=2, decimal_places=1)
    imdbVotes = models.CharField(max_length=30, default='')
    imdbID = models.CharField(max_length=15, default='')
    imdbSeriesID = models.CharField(max_length=15, default='')
    justWatchUrl = models.CharField(max_length=60, default='')

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

    def __str__(self):
        return f"S{self.Season}/E{self.Episode} - {self.Title}"