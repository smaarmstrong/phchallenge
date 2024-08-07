from django import forms
from .models import EnclosureModel

class EnclosureForm(forms.ModelForm):
    class Meta:
        model = EnclosureModel
        fields = ['location', 'height', 'constraint']
        widgets = {
            'location': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-control'}),
            'constraint': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EnclosureForm, self).__init__(*args, **kwargs)
        # Set 'Not applicable' as default initial value
        self.fields['location'].initial = 'not_applicable'
        self.fields['height'].initial = 'not_applicable'
        self.fields['constraint'].initial = 'not_applicable'