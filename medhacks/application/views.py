from django.views.generic import TemplateView
from application.forms import ApplicationForm
from application.models import ApplicationModel
from django.shortcuts import render, redirect

from django.http import HttpResponse

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
        form = ApplicationForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
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
            return render(request, 'application/applied.html')
        return render(request, self.template_name, {'form': form})


        #First parameter is namespace we created and specified in medhacks.urls
        #second parameter is 'name' we specified in application.urls
        #This way we can avoid hardcoded urls
        # return redirect('accounts_namespace:view_profile')
