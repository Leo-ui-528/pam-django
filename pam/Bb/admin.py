from django.contrib import admin
from .models import Bb
from .models import Owner
from. models import City
from. models import District
from. models import Type_of_doing
from. models import Type_of_objects
from. models import Gz
from. models import Customers
from. models import Directions
from. models import Diovisions
from. models import Assignments
from. models import Doc


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
admin.site.register(City)
admin.site.register(District)
admin.site.register(Type_of_doing)
admin.site.register(Type_of_objects)
admin.site.register(Gz)
admin.site.register(Customers)
admin.site.register(Directions)
admin.site.register(Diovisions)
admin.site.register(Assignments)
admin.site.register(Doc)
