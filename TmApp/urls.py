from django.urls import path
from TmApp.views import *


urlpatterns = [
    path('', index, name='tmIndex'),
]
