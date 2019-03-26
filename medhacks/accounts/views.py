from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Matt kim'
    args = {'Name': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args) #django automatically looks
    #for a templates folder, that's why we make an additional accounts folder
    #Third parameter in render is the data we want to pass through

#obviously this is view for registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):

    #If user presses the 'submit' button in the edit_profile html page
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
