from django import forms
from .models import Contact

# update form
class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=False)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), required=False)
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}), required=False)
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}), required=False)
    address_1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address 1'}), required=False)
    address_2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address 2'}), required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'City'}), required=False)
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'State'}), required=False)
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'zipcode'}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Country'}), required=False)
    image = forms.ImageField(label="")
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'address_1', 'address_2', 'city', 'state', 'zipcode', 'country', 'image')