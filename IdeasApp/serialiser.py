from rest_framework import serializers

from .models import Idea, Vote


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ["id", "title", "description", "status"]


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ["idea", "comment"]
