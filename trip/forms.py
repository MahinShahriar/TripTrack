from django import forms
from .models import Trip


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