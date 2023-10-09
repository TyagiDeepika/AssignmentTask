from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import User,UserManager,Company



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('details/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def details_view(request):
    user_data = User.objects.all()
    return render(request, 'details.html',{'user_data':user_data})


def update_record(request, id):

    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = AuthenticationForm()

    return render(request, 'update.html',{'form':form})
