import uuid
from django.db import models
from django.contrib.auth.models import User
from helper.some_model import CrUpBase

# Create your models here.
"""
    We will be using JWTTokenAuthntication
    1. Account [post save user. create via signal] 
"""
class Account(CrUpBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"

class AccountAddress(CrUpBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=30)
    is_default = models.BooleanField(default=False)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_add = models.TextField()
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.account.user.username}: {self.city} {self.state} {self.pin_code}"
    