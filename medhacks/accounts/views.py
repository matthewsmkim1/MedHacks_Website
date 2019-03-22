from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Matt kim'
    args = {'Name': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args) #django automatically looks
    #for a templates folder, that's why we make an additional accounts folder
    #Third parameter in render is the data we want to pass through

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
