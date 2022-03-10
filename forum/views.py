from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):

    context_dict = {'boldmessage': 'Hot Posts, Sale of Used Items, Flats to Rent, Activities, Universities, Coffee Break'}

    return render(request, 'forum/index.html', context=context_dict)