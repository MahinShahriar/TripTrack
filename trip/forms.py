from django import forms
from .models import Trip, Note


class CreateTripForm(forms.ModelForm):
    city = forms.CharField(label="City", max_length=20)
    country = forms.CharField(
        label="Country",
        max_length=3,  # Adjusted for ISO country codes
        widget=forms.TextInput(attrs={"placeholder": "example: BD, UAE, US, CAN"})
    )
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Specify the input format
        widget=forms.TextInput(attrs={
            'placeholder': 'dd/mm/yyyy',  # Placeholder text
        }),
        label='Start Date',  # Custom label
    )
    end_date = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Specify the input format
        widget=forms.TextInput(attrs={
            'placeholder': 'dd/mm/yyyy',  # Placeholder text
        }),
        label='End Date',  # Custom label
        required=False  # make the field not required
    )

    class Meta:
        model = Trip
        fields = ['city', 'country', 'start_date', 'end_date']

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['trip', 'title', 'description', 'type', 'img']
        # max image size 5MB
        def clean_img(self):
            img = self.cleaned_data.get('img', False)
            if img:
                if img.size > 5*1024*1024:
                    raise forms.ValidationError("Image file too large ( > 5MB )")
            return img
