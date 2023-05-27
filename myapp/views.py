from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegistrationForm

def Home(request):
    return render(request, 'home.html')


from django.contrib.auth import authenticate, login
from .models import UserCredentials

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            user_credentials = UserCredentials(user=user, username=username, password=password)
            user_credentials.save()
            
            return redirect('Home/')
        
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # Create a new User
            user = User.objects.create_user(username=username, password=password)
            # Create UserProfile
            user_profile = UserProfile(user=user, email=email)
            user_profile.save()

            return redirect('Login')  # Replace 'login' with the name of your login page URL pattern
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})
