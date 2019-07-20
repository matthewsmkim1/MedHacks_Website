from django.conf.urls import url
from django.urls import path, include
from travel.views import TravelView, RecieptView


app_name = 'home'
urlpatterns = [
    path('', TravelView.as_view(), name='travel'),
    path('receipt_submission/', RecieptView.as_view(), name='receipt')
]
