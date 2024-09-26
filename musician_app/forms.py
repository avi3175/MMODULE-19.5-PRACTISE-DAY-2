
from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if self.user is None:
            raise forms.ValidationError("User must be authenticated to submit this form.")

        if first_name != self.user.first_name or last_name != self.user.last_name:
            raise forms.ValidationError("First Name and Last Name must match your user profile.")

        return cleaned_data
