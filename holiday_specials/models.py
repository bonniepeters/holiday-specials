from django.db import models

GENRE_CHOICES = (
    ('comedy','Comedy'),
    ('drama', 'Drama'),
)

STREAMING_CHOICES = {
    ('netflix', 'Netflix'),
    ('hulu', 'Hulu'),
    ('amazon prime', 'Amazon Prime'),
    ('hbo', 'HBO'),
    ('other', 'Other'),
}

class Show(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    streaming_on = models.CharField(max_length=20, choices=STREAMING_CHOICES, default='netflix')
    image_url = models.TextField()
    imdb_url = models.TextField()
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='comedy')

    def __str__(self):
        return self.name

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='episodes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.PositiveIntegerField(default=1)
    episode = models.PositiveIntegerField(default=1)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"S{self.season}/E{self.episode} - {self.name}"