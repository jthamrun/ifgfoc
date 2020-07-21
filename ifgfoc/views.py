from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ifgfoc/index.html")

def aboutUs(request):
    return render(request, "ifgfoc/aboutUs.html")

def give(request):
    return render(request, "ifgfoc/give.html")

def careGroup(request):
    return render(request, "ifgfoc/careGroup.html")

def stream(request):
    return render(request, "ifgfoc/stream.html")