from django.contrib import admin

from TailTales.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'breed', 'age', 'weight', 'owner')
    list_filter = ('species',)
    search_fields = ('name', 'breed', 'owner__username')
    ordering = ('name', 'species')
    list_per_page = 20