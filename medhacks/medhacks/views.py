from django.shortcuts import redirect

def login_redirect(request):
    #if logged in
        #redirect to profile page?
    #else
    if request.user.is_authenticated:
        return redirect('/application')
    else:
        return redirect('/accounts/login')
