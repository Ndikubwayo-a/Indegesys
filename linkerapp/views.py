import datetime

from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.

def index(request):
    current_datetime: datetime.datetime.now()

    context = {'name': 'Albert',
               'website': {'domain': 'www.albert.com', 'ipadress': '128.4.5.5'},
               'ages': '22'

               }
    return render(request, 'pages/index.html', context)


def timedate(request):
    current_datetime: datetime.datetime.now()
    return HttpResponse(current_datetime)


def createaccount(request):
    return render(request, 'createAccount.html')
