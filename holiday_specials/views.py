from rest_framework import generics
from .serializers import ShowSerializer, EpisodeSerializer
from .models import Show, Episode

class ShowList(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowCreate(generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class EpisodeList(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer