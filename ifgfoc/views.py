from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ifgfoc/index.html")

def aboutUs(request):
    return render(request, "ifgfoc/aboutUs.html")

def give(request):
    return render(request, "ifgfoc/give.html")

def caregroup(request):
    return render(request, "ifgfoc/care-group.html")

def stream(request):
    return render(request, "ifgfoc/stream.html")