from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext as _

class HomePage(generic.TemplateView):
    template_name = "home.html"

class PortfolioPage(generic.TemplateView):
    template_name = "portfolio.html"

class ServicesPage(generic.TemplateView):
    template_name = "services.html"

class WhyUsPage(generic.TemplateView):
    template_name = "whyus.html"

class ContactPage(generic.TemplateView):
    template_name = "about.html"

class Login(AuthenticationForm):
    username = forms.CharField(label=("Email"), max_length=75)
    template_name = 'login.html'

def Logout(request):
    logout(request)
    return redirect('/')