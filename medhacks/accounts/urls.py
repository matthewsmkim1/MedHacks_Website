'''
All urls that will be handled by the accounts app will
be in this file

Good documentation: https://django.readthedocs.io/en/2.1.x/topics/auth/default.html
'''

'''

ALSO, RESETTING PASSWORD IS NOT COMPLETED

'''
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
app_name = 'accounts'

'''
Might get a problem with reset-password links. We use default django reset password view.
When we use Django URL namespace, we need to pass along namespace in parameter.
If we have trouble, look in tutorial number 31
'''

#names in the path is used for reverse path, to avoid hardcoded urls.
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'), #this means that accounts/ will render the register function in the views file in accounts
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='reset_password'), #RESETTING PASSWORD NOT COMPLETED!!!!!!!!!!!!
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_complete'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
