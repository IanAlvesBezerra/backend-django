from django.contrib import admin
from toys.models import Toy

# Register your models here.

class ToyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'toy_category',
        'release_date',
    ]
    search_fields = [
        'name',
        'toy_category',
    ]
    list_filter = [
        'toy_category',
        'release_date',
        'was_included_in_home',
    ]

admin.site.register(Toy, ToyAdmin)