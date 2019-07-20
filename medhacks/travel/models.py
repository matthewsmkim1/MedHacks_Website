from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .formatcheck import ContentTypeRestrictedFileField
from datetime import datetime

# Create your models here.
class TravelAppModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default = 'NA')
    country = models.CharField(max_length=50)
    tr_essay = models.CharField(max_length=100, default = '-')
    contribution_essay = models.CharField(max_length=150)
    submit_time = models.DateTimeField(auto_now_add=True)
    type_reim = models.CharField(max_length=5, default = '-')
    # below starts the travel receipts
    first_name = models.CharField(max_length=50, default='-')
    last_name = models.CharField(max_length=50, default='-')
    # Permanent Address
    permanent_address1 = models.CharField(max_length=100, default='-',blank=True, null=True)
    permanent_address2 = models.CharField(max_length=100, default='-', blank=True, null=True)
    permanent_city = models.CharField(max_length=50, default='-',blank=True, null=True)
    permanent_state = models.CharField(max_length=50, default='-', blank=True, null=True)
    permanent_zip = models.CharField(max_length=15, default='-', blank=True, null=True)

    travel_date_from = models.DateTimeField(blank=True, null=True)
    travel_date_to = models.DateTimeField(blank=True, null=True)
    travel_location_city = models.CharField(max_length=50, default='-')
    travel_location_state = models.CharField(max_length=50, default = 'NA')
    receipt_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    reimburse_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    receipt_file = ContentTypeRestrictedFileField(upload_to='receipts', default='-', content_types=['application/pdf','application/docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/doc','image/jpeg'],max_upload_size=2097152,blank=False, null=False)
    policy_check = models.BooleanField(default=False)
