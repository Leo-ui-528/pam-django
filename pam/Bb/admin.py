from django.contrib import admin
from .models import Bb
from .models import Owner


class BbAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'published', 'owner')
    list_display_links = ('name', 'owner')
    search_fields = ('name',)


class Own(admin.ModelAdmin):
    list_display = ('owner',)
    list_display_links = ('owner',)
    search_fields = ('owner',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Owner, Own)
