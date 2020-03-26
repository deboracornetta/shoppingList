from django import forms

class ListingForm(forms.Form):
    text = forms.CharField(max_length=50, 
    widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Things to Buy'
    }
    ))