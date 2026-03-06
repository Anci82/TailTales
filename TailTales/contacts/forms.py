from django import forms

from TailTales.contacts.models import ServiceContact


class ServiceContactForm(forms.ModelForm):
    class Meta:
        model = ServiceContact
        fields = (
            'contact_type',
            'name',
            'phone',
            'email',
            'address',
            'notes',
        )