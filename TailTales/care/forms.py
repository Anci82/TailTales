from django import forms

from TailTales.care.models import Appointment, PreventiveCare, PreventiveCareDose
from TailTales.contacts.models import ServiceContact
from TailTales.pets.models import Pet


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('pet', 'service_contact', 'title', 'date', 'notes', 'is_completed')

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)
            self.fields['service_contact'].queryset = ServiceContact.objects.filter(owner=user)


class PreventiveCareForm(forms.ModelForm):

    class Meta:
        model = PreventiveCare
        fields = (
            'pet',
            'care_type',
            'product_name',
            'interval_days',
            'last_given_date',
            'notes',
        )

        widgets = {
            'last_given_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)

class PreventiveCareDoseForm(forms.ModelForm):
    class Meta:
        model = PreventiveCareDose
        fields = ('given_date', 'notes')
        widgets = {
            'given_date': forms.DateInput(attrs={'type': 'date'}),
        }