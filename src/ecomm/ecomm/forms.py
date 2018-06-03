from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control", "placeholder":"Your Full Name"}))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class":"form-control", "placeholder":"Your Email"}))
    content = forms.CharField(widget = forms.Textarea(attrs = {"class":"form-control", "placeholder":"Your message!"}))


    def clean_email(self):

        email = self.cleaned_data.get("email")
        if "edu" not in email:

            raise forms.ValidationError("email in invalid.")

        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label = "confirm password", widget=forms.PasswordInput)
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Full Name"}))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if(password != password2):
            raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_email(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username already exists.")
        return username