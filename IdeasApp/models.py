from django.contrib.auth.models import User
from django.db.models import *

Status_list = [
    ("Waiting", "Waiting"),
    ("Accepted", "Accepted"),
    ("Denied", "Denied"),
    ("Done", "Done")
]


class Idea(Model):
    title = CharField(max_length=255)
    description = TextField()
    status = CharField(choices=Status_list, max_length=30, default="Waiting")

    def __str__(self):
        return self.title


class Vote(Model):
    # XXX: Change to normal user
    author = User
    idea = ForeignKey(Idea, on_delete=CASCADE)
    comment = TextField()

    def __str__(self):
        return f"Vote for: {self.idea}"
