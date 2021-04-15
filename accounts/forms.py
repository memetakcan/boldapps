from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Şifre", widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola hatalı!")
            return super(LoginForm,self).clean()