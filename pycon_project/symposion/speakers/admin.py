from django.contrib import admin

from symposion.speakers.models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "twitter_username", "sessions_preference", 'has_photo', "created"]
    search_fields = ["name"]

    def has_photo(self, obj):
        return obj.photo != ''
    has_photo.boolean = True

admin.site.register(Speaker, SpeakerAdmin)
