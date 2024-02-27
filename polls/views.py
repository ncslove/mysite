from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. 다시 한번 you're at the 에렵다. polls index.")
