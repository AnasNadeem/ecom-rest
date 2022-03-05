from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from authen.models import Account, AccountAddress
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def post_save_create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)