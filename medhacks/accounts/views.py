from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

#obviously this is view for registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args) #django automatically looks
    #for a templates folder, that's why we make an additional accounts folder
    #Third parameter in render is the data we want to pass through

@login_required
def edit_profile(request):

    #If user presses the 'submit' button in the edit_profile html page
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            #First parameter is namespace we created and specified in medhacks.urls
            #second parameter is 'name' we specified in accounts.urls
            #This way we can avoid hardcoded urls
            return redirect(reverse('accounts_namespace:view_profile'))
        else:
            return redirect(reverse('accounts_namespace:edit_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts_namespace:view_profile'))
        else:
            return redirect(reverse('accounts_namespace:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
