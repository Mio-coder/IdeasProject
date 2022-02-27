from django.urls import path, include
from rest_framework import routers

from .views import VoteViewSet, IdeaViewSet
from .views import index

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'Votes', VoteViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("auth-api/", include("rest_framework.urls", namespace="rest_framework")),
    # path("", index),
]
