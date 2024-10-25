from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout


from accounts.forms import CustomUserCreationForm

def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/index.html', context)


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('stores:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth_login(request)
            return redirect('stores:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form':form
        }
        return render(request, 'accounts/signup.html', context)