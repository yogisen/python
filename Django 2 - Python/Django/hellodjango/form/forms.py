from django import forms


class TestForm(forms.Form):
    CITIES_CHOICES = (
        (0, 'Paris'),
        (1, 'Toulouse'),
        (2, 'Lyon'),
    )

    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your email', required=False, max_length=50)
    yes_no = forms.BooleanField(label='Either Yes or No')
    city = forms.ChoiceField(label='Your city', choices=CITIES_CHOICES)

