from django.urls import path
from application import views

app_name = 'application'

urlpatterns = [
    path('', views.application, name='application')
]
