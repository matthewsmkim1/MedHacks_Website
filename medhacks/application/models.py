from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .formatChecker import ContentTypeRestrictedFileField
# Create your models here.
class ApplicationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='-')
    last_name = models.CharField(max_length=50, default='-')
    email = models.EmailField(max_length=50, default='-')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, default='-')
    city = models.CharField(max_length=50, default = '-')
    state = models.CharField(max_length=50, default = 'NA')
    country = models.CharField(max_length=50, default='-')
    birthday = models.CharField(max_length=100, default='-')
    gender = models.CharField(max_length=50, default='-')
    race = models.CharField(max_length=50, default='-')
    education = models.CharField(max_length=20, default = '-')
    university = models.CharField(max_length=100, default='-')
    graduating_class = models.CharField(max_length=50, default='NA')
    major = models.CharField(max_length=50, default='-')
    secondmajor = models.CharField(max_length=50, default = 'NA')
    reimbursement = models.CharField(max_length=50, default = 'No')
    essay1 = models.CharField(max_length=350, default = '-')
    essay2 = models.CharField(max_length=350, default = '-')
    essay3 = models.CharField(max_length=350, default = '-')
    essay4 = models.CharField(max_length=350, default = '-')
    reimbursement = models.CharField(max_length=50, default='No')
    attended = models.CharField(max_length=50, default = 'No')
    resume = ContentTypeRestrictedFileField(upload_to='resume', content_types=['application/pdf','application/docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/doc','image/jpeg'],max_upload_size=2097152,blank=False, null=False)
    permission = models.BooleanField(default=True)
    conduct = models.BooleanField(default=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    how_heard_medhacks = models.CharField(max_length=50, default='-')

class Meta:
    ordering = ['first_name']
