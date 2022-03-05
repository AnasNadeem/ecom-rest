from authen.views import (
    RegsiterAPI, 
    LoginAPI, 
    AccounstAddressViewset
)
from django.urls import path, include

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'account_address', AccounstAddressViewset, basename='account_address')

urlpatterns = [
    path('register/', RegsiterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path("", include(router.urls)),
]
