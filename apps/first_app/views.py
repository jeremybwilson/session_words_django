from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import strftime
from datetime import datetime

# Create your views here.
def index(request):

    return render(request, 'first_app/index.html')

def process(request):
    request.session['date_time'] = datetime.now().strftime('%H:%M:%S%p, %B %d %Y')
    date_time = request.session['date_time']
    print "*" * 80
    print "Here is the current date/time: ", date_time

    if request.method == "POST":
        request.session['date_time'] = datetime.now().strftime('%H:%M:%S%p, %B %d %Y')
        date_time = request.session['date_time']
        
        print "*" * 80
        print "Here is the current date/time: ", date_time

        if 'words' not in request.session:
            request.session['words'] = []
        if 'bigfont' in request.POST:
            data = {
                'session_word': request.POST['session_word'],
                'session_color': request.POST['session_color'],
                'session_font': 'strong',
                'session_time': date_time
            }
        else:
            data = {
                'session_word': request.POST['session_word'],
                'session_color': request.POST['session_color'],
                'session_font': 'default',
                'session_time': date_time
            }
        # session_word = request.POST['session_word']
        # session_color = request.POST['session_color']
        print "Here is the passed form information: ", request.POST

        request.session['words'].append(data)
        request.session.modified = True

        print request.session['words']

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')