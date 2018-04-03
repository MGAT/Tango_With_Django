from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("rango says here is the about page. <a href='/rango/'>Index</a>")