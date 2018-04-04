from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cipcake'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("rango says here is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', {})