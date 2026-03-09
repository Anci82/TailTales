from django.contrib import admin

from TailTales.care.models import Appointment, PreventiveCare, PreventiveCareDose


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pet', 'date', 'is_completed', 'service_contact')
    list_filter = ('is_completed', 'date')
    search_fields = ('title', 'pet__name', 'service_contact__name')
    ordering = ('date', 'title')
    list_per_page = 20


class PreventiveCareDoseInline(admin.TabularInline):
    model = PreventiveCareDose
    extra = 0


@admin.register(PreventiveCare)
class PreventiveCareAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'care_type', 'product_name', 'last_given_date', 'next_due_date')
    list_filter = ('care_type', 'next_due_date')
    search_fields = ('pet__name', 'product_name')
    ordering = ('next_due_date', 'care_type')
    list_per_page = 20
    inlines = [PreventiveCareDoseInline]