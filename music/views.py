from django.shortcuts import render
from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MusicFilter
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend]  # Use filters instead of filter
    filterset_class = MusicFilter

    def list(self, request: Request) -> Response:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)