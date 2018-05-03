from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import inlineformset_factory, modelformset_factory, ModelForm
from .forms import UserSignupForm, ProfileSignupForm
from .models import *
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, viewsets
from serializer import CustomerProfileSerializer, UserSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework import generics


def Signup(request):
    if request.user.is_authenticated():
        return redirect("/landing/", request.user)
    user_form = UserSignupForm(request.POST or None)
    profile_form = ProfileSignupForm(request.POST or None)
    user = None
    if user_form.is_valid() & profile_form.is_valid():
        new_user=User.objects.create_user(user_form.cleaned_data['email'],
        user_form.cleaned_data['email'],
        user_form.cleaned_data['password1'])
        new_user.first_name = user_form.cleaned_data['first_name']
        new_user.last_name = user_form.cleaned_data['last_name']
        new_user.save()
        profile = CustomerProfile()
        profile.user = new_user
        profile.address = profile_form.cleaned_data['address']
        profile.city = profile_form.cleaned_data['city']
        profile.state = profile_form.cleaned_data['state']
        profile.zip_code = profile_form.cleaned_data['zip_code']
        profile.phone_number = profile_form.cleaned_data['phone_number']
        profile.save()
        user = authenticate(
            username=new_user.username,
            password=user_form.cleaned_data['password1'])
        if user:
            login(request, user)
            return redirect("/landing/")

    template = "signup.html"
    context = {
        "userform": user_form,
        "profileform": profile_form,
        "user": user
    }
    return render(request, template, context)


def Landing(request):
    template = "landing.html"
    ReferralInlineFormSet = inlineformset_factory(CustomerProfile, Referral,
                                                  fields=[
                                                      'first_name',
                                                      'last_name',
                                                      'phone_number',
                                                      'email'
                                                  ],
                                                  extra=1
                                                  )

    customer = CustomerProfile.objects.get(pk=request.user.customerprofile.pk)
    mailformset = ProfileSignupForm(instance=customer)

    # ReferralInlineFormSet += inlineformset_factory(CustomerProfile, Estimate, fields='__all__', extra=1)
    if request.method == "POST":
        formset = ReferralInlineFormSet(request.POST, request.FILES, instance=customer)
        mailformset = ProfileSignupForm(request.POST, instance=customer)
        if formset.is_valid() & mailformset.is_valid():
            formset.save()
            mailformset.save()
            formset = ReferralInlineFormSet(instance=customer)
            mailformset = ProfileSignupForm(instance=customer)
            # Do something. Should generally end with a redirect. For example:
            return render(request, template, {'formset': formset,
                                              'mailingform': mailformset})
    else:
        formset = ReferralInlineFormSet(instance=customer)
        mailformset = ProfileSignupForm(instance=customer)
    return render(request, template, {'formset': formset,
                                      'mailingform': mailformset})


class user_list(generics.ListCreateAPIView):

    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

class user_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

