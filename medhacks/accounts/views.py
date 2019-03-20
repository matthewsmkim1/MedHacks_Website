from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Matt kim'
    args = {'Name': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args) #django automatically looks
    #for a templates folder, that's why we make an additional accounts folder
    #Third parameter in render is the data we want to pass through
