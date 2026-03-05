from django.contrib import admin

from TailTales.contacts.models import ServiceContact


@admin.register(ServiceContact)
class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_type', 'phone', 'email', 'owner')
    list_filter = ('contact_type',)
    search_fields = ('name', 'phone', 'email', 'owner__username')
    ordering = ('contact_type', 'name')
    list_per_page = 20