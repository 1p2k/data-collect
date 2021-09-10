import requests
from django import forms
from django.conf import settings

from ..core.forms import BootstrapFormMixin
from .models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    recaptcha = forms.CharField(
        max_length=1024,
        required=False,
        widget=forms.HiddenInput(),
    )

    def clean(self):
        cleaned_data = super().clean()
        recaptcha_data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': cleaned_data.get('recaptcha'),
        }

        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)
        result = response.json()

        if result.get('success') and result.get('score') > 0.5:
            # print(result.get('score'))
            pass
        else:
            raise forms.ValidationError('You are not a human!')

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
