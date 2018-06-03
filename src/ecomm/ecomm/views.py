# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login

def home_page(request):
    home = {"heading": "Welcome to the home page!",
            "premium_content": "THIS IS PREMIUM CONTENT"}
    return render(request, "home_page.html", home)


def about_page(request):
    about = {"heading" : "This is the about page!"}
    return render(request, "home_page.html", about)

def contact_page(request):
    # If there's some data entered into the form, pass that data. Else None. If none, following If condition is not executed.
    contact_form = ContactForm(request.POST or None)
    contact = {"heading": "Welcome to the contact page.",
               "form": contact_form}
    if contact_form.is_valid():
        print(contact_form.cleaned_data);

    # Extracting values submitted by the user in the form
    if request.method == "POST":
        print(request.POST.get("fullname"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))
    return render(request, "home_page.html", contact)

def login_page(request):
    login_class = LoginForm(request.POST or None)
    login_context = {"form": login_class}
    print("User logged in:")
    print(request.user.is_authenticated)
    if login_class.is_valid():
        data = login_class.cleaned_data
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username = username, password = password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print("User logged in:" )
            print(request.user.is_authenticated)
            return redirect("/login")
        else:
            print("Error")


    return render(request, "auth/loginform.html", login_context)

def register_page(request):
    register_class = RegisterForm(request.POST or None)
    register_context = {"form": register_class}
    if register_class.is_valid():
        data = register_class.cleaned_data
        print(data)
        # username = data.get("username")
        # password = data.get("password")
        # password2 = data.get("password2")
        # fullname = data.get("fullname")
        # email = data.get('email')
    return render(request, "auth/register.html", register_context)

