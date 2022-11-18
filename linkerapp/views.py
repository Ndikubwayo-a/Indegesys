from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib import messages


# Create your views here.

def index(request):
    context = {'name': 'Albert',
               'website': {'domain': 'www.albert.com', 'ipadress': '128.4.5.5'},
               }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def tournament(request):
    return render(request, 'tournaments.html')


def footballclubs(request):
    return render(request, 'foot clubs.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"errors": "There was an  error trying to login. Try Again ....."}

            return render(request, "login.html", context)

        dj_login(request, user)
        return redirect('index')

    return render(request, 'login.html', {})


def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect('logout')
    return render(request, 'logout.html', {})
