from django.shortcut import render
from django.http import HttpsResponse

def index(request):
    return HttpResponse("<h1>Welcome</h1>")
def about(request):
    return HttpResponse("<h1>about page</h1>")