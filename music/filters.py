from django_filters import rest_framework as django_filters
from .models import Music  # Add this line

class MusicFilter(django_filters.FilterSet):
    class Meta:
        model = Music
        fields = ['titulo', 'artista', 'album', 'genero']  # adjust fields to filter on