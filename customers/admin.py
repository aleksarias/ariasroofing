from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

from customers.models import CustomerProfile


# Define an inline admin descriptor for UserProfile model
class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = True

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (CustomerProfileInline, )

class EstimateInline(admin.StackedInline):
    model = Estimate
    extra = 0

class JobInline(admin.StackedInline):
    model = Job
    extra = 0

class ReferralInline(admin.StackedInline):
    model = Referral
    extra = 0

class AdminCustomerProfile(admin.ModelAdmin):
    inlines = [
        EstimateInline,
        JobInline,
        ReferralInline,
    ]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin,)
admin.site.register(CustomerProfile, AdminCustomerProfile)
admin.site.register(Estimate)
admin.site.register(Job)
admin.site.register(Referral)