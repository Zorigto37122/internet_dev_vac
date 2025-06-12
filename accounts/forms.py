from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control my-custom-username-class'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control my-custom-email-class'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control my-custom-password-class'
        })
        self.fields['password_confirm'].widget.attrs.update({
            'class': 'form-control my-custom-passwordconfirm-class'
        })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ''
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ''
        })