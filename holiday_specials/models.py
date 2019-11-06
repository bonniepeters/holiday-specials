from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    streaming_on = models.CharField(max_length=60)
    image_url = models.TextField()
    imdb_url = models.TextField()
    genre = models.CharField(max_length = 60)

    def __str__(self):
        return self.name

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='episodes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.IntegerField()
    episode = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"S{self.season}/E{self.episode} - {self.name}"