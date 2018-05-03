from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerProfile(models.Model):
    user = models.OneToOneField(User)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=7, default='Florida')
    zip_code = models.IntegerField()
    def __unicode__(self):
        return '%s, %s' % (self.user.last_name, self.user.first_name)


class Estimate(models.Model):
    estimate_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerProfile, null=True, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=7, default='Florida')
    zip_code = models.IntegerField()
    description = models.TextField(max_length=500, default='')

    def __unicode__(self):
        return '%s-%s-%s' % (self.estimate_id, self.address, self.customer.user.last_name)


class Job(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    job_id = models.AutoField(primary_key=True)
    estimate_id = models.OneToOneField(Estimate)

    def __unicode__(self):
        return '%s-%s-%s' % (self.customer, self.job_id, self.estimate_id)


class Referral(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    referral_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, blank=True)
    estimate_id = models.OneToOneField(Estimate, blank=True, null=True)

    def __unicode__(self):
        return '%s-%s' % (self.referral_id, self.customer.user.last_name)

# class EstimateItem(models.Model):
#     estimate = models.ForeignKey(Estimate)
#     estimate_item_id = models.AutoField(primary_key=True)
#     item_description = models.TextField(max_length=500)
#     item_price = models.DecimalField(decimal_places=2)

# Import all signal triggers
from signals import *
