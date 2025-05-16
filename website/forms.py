from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        
        
    # sign up form
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=False)
#     last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), required=False)
#     email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email'}), required=False)
    
#     class Meta: 
#         model = User
#         feilds = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password1'].label = ''
#         self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['password2'].label = ''
#         self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'