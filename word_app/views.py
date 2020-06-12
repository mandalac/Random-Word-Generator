from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'index.html')

def random(request):
    try:
        request.session['counter'] +=1
    except:
        request.session['counter'] =1

    context = {
        'word': get_random_string(length=14)
    }
    return render(request, 'index.html',context)

def restart(request):
    del request.session['counter']
    return redirect('/random')