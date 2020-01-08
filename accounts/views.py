from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        #user is signing up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['email'])
                return render(request, 'accounts/signup.html', {'error':'Email already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'],request.POST['email'],
                request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})

    else:
        #user is entering data
        return render(request, 'accounts/signup.html')

    #return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        try:
            user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'error':'Email or Password entered is incorrect'})
        except:
            return render(request, 'account/login.html', {'error':'Unknown error'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    #TODO fix this after, no need for an actual template page here
    # route to home page and logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    