from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Service

# Create your views here.
def home(request):
    return HttpResponse('<style>body{background-color: gray}</style><h1>Home</h1><h1>Search Form</h1><h1>List Searched</h1>')

def history(request):
    movies = Movie.objects.all()
    data = {'movies': movies }
    return render(request, 'where_to_watch/history.html', data)