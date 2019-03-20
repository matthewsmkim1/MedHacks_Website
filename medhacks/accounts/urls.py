'''
All urls that will be handled by the accounts app will
be in this file
'''

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.home), #this means that accounts/ will render the home function in the views file in accounts
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login")
]
