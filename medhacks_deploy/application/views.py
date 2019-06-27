from django.views.generic import TemplateView
from application.forms import ApplicationForm
from application.models import ApplicationModel
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.http import HttpResponse

import logging
import boto3
from botocore.exceptions import ClientError

class ApplicationView(TemplateView):
    template_name = 'application/application.html'

    def get(self, request):
        ufirst_name = request.user.first_name;
        ulast_name = request.user.last_name;
        uemail = request.user.email;
        #this applicationForm is the one we created in the forms.py file. Self explanatory
        form = ApplicationForm(initial={'first_name':ufirst_name, 'last_name':ulast_name, 'email':uemail})
        application = ApplicationModel.objects.filter(user=request.user)[:1]

        # If the user has already applied
        if application.count() > 0:
            return render(request, 'application/applied.html')

        # If the user has not applied yet
        return render(request, self.template_name, {'form': ApplicationForm})

    def post(self, request):
        #This initializes and creates a form with the data that was received in the post request
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print(post.user.username)
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            race = form.cleaned_data['race']
            education = form.cleaned_data['education']
            university = form.cleaned_data['university']
            gclass = form.cleaned_data['graduating_class']
            major = form.cleaned_data['major']
            secondmajor = form.cleaned_data['secondmajor']
            attended = form.cleaned_data['attended']
            reimbursement = form.cleaned_data['reimbursement']
            essay1 = form.cleaned_data['essay1']
            essay2 = form.cleaned_data['essay2']
            essay3 = form.cleaned_data['essay3']
            essay4 = form.cleaned_data['essay4']
            how_heard_medhacks = form.cleaned_data['how_heard_medhacks']
            permission = form.cleaned_data['permission']
            conduct = form.cleaned_data['conduct']
            form.save()

            # send email

            mail_subject = 'Thank you for applying to Medhacks!'
            message = render_to_string('application/submission_email.html', {
                'firstname': first,
            })
            to_email = form.cleaned_data.get('email')
            email_obj = EmailMessage(mail_subject, message, to=[email])
            email_obj.send()

            #upload to s3 here
            #https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html

            s3_client = boto3.client('s3')
            object_name = request.FILES.get('resume')
            bucket = 'medhacks-2019-resumes'
            file_name = request.FILES
            file_overwrite = False


            #test@1 - fails
            #test.1
            #test+1 - fails

            remove_weird_char_name = post.user.username.replace('@', '');
            remove_weird_char_name = remove_weird_char_name.replace('+', '')

            s3 = boto3.client('s3')
            # s3_client.upload_file(settings.RESUME_ROOT + post.user.username + '-' + request.FILES.get('resume').name.replace(' ', '_'),
            #     bucket, str(post.user.username + '-' + request.FILES.get('resume').name.replace(' ', '_')))


            s3_client.upload_file(settings.RESUME_ROOT + remove_weird_char_name + '-' + request.FILES.get('resume').name.replace(' ', '_'),
                bucket, str(post.user.username + '-' + request.FILES.get('resume').name.replace(' ', '_')))




            #Enforce unique file names
            #https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django

            return render(request, 'application/applied.html')
        print(form.errors.as_data())
        return render(request, self.template_name, {'form': form})


        #First parameter is namespace we created and specified in medhacks.urls
        #second parameter is 'name' we specified in application.urls
        #This way we can avoid hardcoded urls
        # return redirect('accounts_namespace:view_profile')
