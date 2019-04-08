from django import forms
from application.models import ApplicationModel
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
import json, os, csv, pickle

class ApplicationForm(forms.ModelForm):
    path_to_colleges = os.path.join(settings.STATIC_ROOT, 'colleges.pickle')
    path_to_majors = os.path.join(settings.STATIC_ROOT, 'majors.pickle')
    path_to_states = os.path.join(settings.STATIC_ROOT, 'states.pickle')

    with open(path_to_colleges, 'rb') as handle:
        tupled_list_colleges = pickle.load(handle)
    with open(path_to_majors, 'rb') as handle:
        tupled_list_majors = pickle.load(handle)
    with open(path_to_states, 'rb') as handle:
        tupled_list_states = pickle.load(handle)

    races_list = [('Prefer not to answer', 'Prefer not to answer'), ('Indian or Alaskan', 'American Indian or Alaskan Native'), ('Asian', 'Asian/Pacific Islander'),
        ('Black', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White', 'White/Caucasian'),
        ('Multiple', 'Multiple Ethnicity/Other')]

    CHOICESMEDHACKS=[('Yes',' Yes'), ('No',' No')]
    CHOICES_HEARD = [('Facebook', ' Facebook'), ('Instagram', ' Instagram'), ('MLH', ' MLH'),
                    ('Campus Ambassador', ' MedHacks Campus Ambassador'),('Email', ' Email'), ('Other', ' Other')]

    first_name = forms.CharField(label='First Name', max_length=50, widget = forms.HiddenInput())
    last_name = forms.CharField(label='Last Name', max_length=50, widget = forms.HiddenInput())
    email = forms.EmailField(label='Email', max_length=50, widget = forms.HiddenInput())
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    city = forms.CharField(label="City", max_length=50)
    state = forms.ChoiceField(label='State', choices=tupled_list_states)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('Prefer not to say', 'Prefer not to say')))
    race = forms.ChoiceField(label='Race', choices=races_list)
    education = forms.ChoiceField(label='Current Level of Education', choices =
        (('High School', 'High School'), ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'), ('Professional', 'Professional')))
    university = forms.ChoiceField(label='University', choices=tupled_list_colleges)
    other_uni = forms.CharField(label='Other University', max_length=100, required=False)
    birthday = forms.CharField(label='Birthday', max_length=100, help_text='Input birthday in form MM/DD/YYYY')
    graduating_class = forms.ChoiceField(label='Graduating Class', choices=(('NA','NA'),('2018','2018'), ('2019','2019'), ('2020','2020'), ('2021+','2021+')))
    major = forms.ChoiceField(label='Major/Area of Expertise', choices=tupled_list_majors)
    secondmajor = forms.ChoiceField(label='Second Major/Area of Expertise', choices=tupled_list_majors, required=False)
    attended = forms.ChoiceField(label='Have you attended MedHacks previously?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    # reimbursement = forms.ChoiceField(label='Will you be seeking a travel reimbursement?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    essay1 = forms.CharField(label='Why do you want to attend MedHacks 2018? (Max 350 characters)', widget=forms.Textarea, max_length=350)
    essay2 = forms.CharField(label='What skills can you bring to the hackathon? (Max 350 characters)', widget=forms.Textarea, max_length=350)
    essay3 = forms.CharField(label='What would you like to see at MedHacks 2018? (Max 350 characters)', widget=forms.Textarea, max_length=350)
    essay4 = forms.CharField(label='Is there anything you would like us to know? (Max 350 characters)', widget=forms.Textarea, required=False, max_length=350)
    resume = forms.FileField(label='Upload Resume', widget = forms.FileInput, required=True)
    how_heard_medhacks = forms.ChoiceField(label='How did you hear about MedHacks 2018', choices=CHOICES_HEARD, widget=forms.RadioSelect())
    permission = forms.BooleanField(label=''' I authorize you to share my application/registration information for event administration, ranking,
         MLH administration, pre- and post-event informational e-mails, and occasional messages about hackathons
         in-line with the MLH Privacy Policy. I further agree to the terms of both the MLH Contest Terms and
         Conditions and the MLH Privacy Policy''',required=True)
    conduct = forms.BooleanField(label=' I have read and agree to the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf"target="_blank">MLH Code of Conduct</a>',required=True)
    # def clean_other_uni(self):
    #     if self.cleaned_data['university'] == 'Other' and self.cleaned_data['other_uni'] == '':
    #         self.cleaned_data['other_uni'] = 'None'
    #         raise ValidationError("Please enter your university")
    #     return self.cleaned_data['other_uni']

    def clean(self):
        if self.cleaned_data['university'] == 'Other':
            if self.cleaned_data['other_uni'] == '':
                self.add_error('other_uni', "Please enter your university")
            else:
                self.cleaned_data['university'] = self.cleaned_data['other_uni']
        # if self.cleaned_data['permission'] == 'False':
        #     self.add_error('Please checkmark this box')

    class Meta:
        model = ApplicationModel

        #Remember to leave a comma at the end
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'city', 'state', 'country', 'birthday', 'gender', 'race',
        'education', 'university', 'other_uni', 'major','secondmajor','graduating_class', 'attended',
        'essay1', 'essay2', 'essay3', 'essay4','how_heard_medhacks','resume', 'permission', 'conduct',
        )
        
