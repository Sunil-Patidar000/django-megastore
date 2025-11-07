from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

