# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from .forms import ContactForm

def home_page(request):
    home = {"heading": "Welcome to the home page!" }
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

