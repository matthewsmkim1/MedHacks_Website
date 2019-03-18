from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/login.html') #django automatically looks
    #for a templates folder, that's why we make an additional accounts folder
