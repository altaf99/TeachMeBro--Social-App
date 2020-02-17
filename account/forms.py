from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserCreateForm(UserCreationForm):
    name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    phone_no = forms.CharField(label="Mobile No", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    
    class Meta:
        fields = ("name","username", "email","phone_no", "password1", "password2")
        model = User

    #to override the default label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["email"].label = "Email address"