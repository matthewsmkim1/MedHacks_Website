'''
All urls that will be handled by the accounts app will
be in this file

Good documentation: https://django.readthedocs.io/en/2.1.x/topics/auth/default.html
'''

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.home), #this means that accounts/ will render the home function in the views file in accounts
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout")
]
