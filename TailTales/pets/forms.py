from django import forms

from TailTales.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'name',
            'species',
            'breed',
            'age',
            'weight',
            'photo_url',
        )


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass