from django.contrib import admin

from TailTales.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image_url')
    search_fields = ('user__username', 'user__email')
    ordering = ('user__username',)
    list_per_page = 20
