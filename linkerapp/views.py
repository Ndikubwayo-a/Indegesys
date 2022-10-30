import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    current_datetime: datetime.datetime.now()

    context = {'name': 'Albert',
               'website': {'domain': 'www.albert.com', 'ipadress': '128.4.5.5'},
               'ages': '22'

               }
    return render(request, 'index.html', context)


def createaccount(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['uphone']
        passw1 = request.POST['pass1']
        passw2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, passw1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(request, "Successfully created")

        return redirect('index.html')
    return render(request, 'createAccount.html')


def signin(request):
    return render(request, 'createAccount.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
