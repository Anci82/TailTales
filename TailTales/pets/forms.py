from django import forms
from TailTales.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'species', 'breed', 'age', 'weight', 'photo_url')
        labels = {
            'age': 'Age (years)',
            'weight': 'Weight (kg)',
            'photo_url': 'Photo URL',
        }
        widgets = {
            'age': forms.NumberInput(attrs={'min': 0, 'placeholder': 'e.g. 3'}),
            'weight': forms.NumberInput(attrs={'min': 0.1, 'step': '0.1', 'placeholder': 'e.g. 22.5'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Rita'}),
            'breed': forms.TextInput(attrs={'placeholder': 'e.g. Husky'}),
            'photo_url': forms.URLInput(attrs={'placeholder': 'https://example.com/photo.jpg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = list(self.fields['species'].choices)
        choices[0] = ('', 'Select species...')
        self.fields['species'].choices = choices


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass