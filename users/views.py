from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        mail = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,'Email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=mail)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('number')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')