from django.urls import path
from application.views import ApplicationView

app_name = 'application'

urlpatterns = [
    path('', ApplicationView.as_view(), name='application')
]
