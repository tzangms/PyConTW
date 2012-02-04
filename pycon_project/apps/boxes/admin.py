from django.contrib import admin

from boxes.models import Box

class BoxAdmin(admin.ModelAdmin):
    list_display = ('label', 'language_code')

admin.site.register(Box, BoxAdmin)
