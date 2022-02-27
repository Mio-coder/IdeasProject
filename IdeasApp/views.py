from django.http import HttpResponse
from rest_framework import viewsets

from .models import Idea, Vote
from .serialiser import IdeaSerializer, VoteSerializer


def index(_):
    return HttpResponse("Hello Django")

# ------------------------------------------


class IdeaViewSet(viewsets.ModelViewSet):
    # noinspection PyUnresolvedReferences
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer


class VoteViewSet(viewsets.ModelViewSet):
    # noinspection PyUnresolvedReferences
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
