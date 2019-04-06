from django.views.generic import TemplateView
from application.forms import ApplicationForm
from django.shortcuts import render, redirect

from django.http import HttpResponse

class ApplicationView(TemplateView):
    template_name = 'application/application.html'

    def get(self, request):
        #this applicationForm is the one we created in the forms.py file. Self explanatory
        form = ApplicationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        #This initializes and creates a form with the data that was received in the post request
        form = ApplicationForm(request.POST)

        if form.is_valid():
            pos = form.save(commit=False)
            pos.user = request.user
            pos.save()
            form = ApplicationForm()
            #change redirect to Thanks for applying page

            #First parameter is namespace we created and specified in medhacks.urls
            #second parameter is 'name' we specified in application.urls
            #This way we can avoid hardcoded urls
            return redirect('application_namespace:application')

        args = {'form': form}
        return render(request, self.template_name, args)
