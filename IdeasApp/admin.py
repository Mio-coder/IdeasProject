from django.contrib import admin

from .models import Idea, Vote


class VoteInline(admin.TabularInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "status"]
    list_filter = ["status"]
    inlines = [
        VoteInline
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["id", "idea", "comment"]
    list_filter = ["idea"]
