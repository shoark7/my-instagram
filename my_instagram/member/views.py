from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, \
                                logout as auth_logout
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth_authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('photo:photo_list')


    else:
        return render(request, 'auth/login.html')

def login_form(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth_authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('photo:photo_list')
            else:
                context['form'] = form
    else:
        context['form'] = LoginForm()
    return render(request, 'auth/login.html', context)



class








################################# log in session ended ###################


def logout(request):
    auth_logout(request)
    return render(request, 'base/common.html')
