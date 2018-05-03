from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.models import CustomerProfile

@receiver(post_save, sender=User)
def handle_user_save(sender, instance, **kwargs):
    if sender:
        print "Got the signal!"
    CustomerProfile(user=instance)

    print "Created profile"
