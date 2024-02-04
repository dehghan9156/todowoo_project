from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserSignUpForm(forms.Form):
    username = forms.CharField(widget =forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget =forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('The username has already been entered')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        password_confirm = cleaned_data.get('password2')
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("The two password fields must match.")
        return cleaned_data

