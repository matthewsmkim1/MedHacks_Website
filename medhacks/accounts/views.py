from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash
# email imports
from accounts.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text


#obviously this is view for registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            print("got here")
            user = form.save()



            # set user to inactive until email is verified
            # user.is_active = True
            user.is_active = False



            # save this field
            user.save()

            # format email information
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user), # token from token generator
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            #change HttpResponse to redirect to an actual web page that says the following
            #return HttpResponse('Please confirm your email address to complete the registration')







            login(request, user)
            return render(request, 'accounts/profile.html', {'user': request.user})
            #return redirect('/accounts/login')
        else:

            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'accounts/reg_form.html', args)
#        return HttpResponse('Your form is not valid')

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

# view for activating user after activation email link is clicked
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

# @login_required
# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'accounts/profile.html', args) #django automatically looks
#     #for a templates folder, that's why we make an additional accounts folder
#     #Third parameter in render is the data we want to pass through

# @login_required
# def edit_profile(request):
#
#     #If user presses the 'submit' button in the edit_profile html page
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             #First parameter is namespace we created and specified in medhacks.urls
#             #second parameter is 'name' we specified in accounts.urls
#             #This way we can avoid hardcoded urls
#             return redirect(reverse('accounts_namespace:view_profile'))
#         else:
#             return redirect(reverse('accounts_namespace:edit_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #First parameter is namespace we created and specified in medhacks.urls
            #second parameter is 'name' we specified in accounts.urls
            #This way we can avoid hardcoded urls
            return redirect(reverse('accounts_namespace:view_profile'))
        else:
            return redirect(reverse('accounts_namespace:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
