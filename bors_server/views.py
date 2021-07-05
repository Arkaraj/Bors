from django.shortcuts import render, HttpResponse
# Create your views here.


def index(request):

    data = {
        'heading': "Doggos"
    }

    return render(request, 'index.html', data)


def users(request):
    return render(request, 'user.html')
