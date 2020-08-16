from django.http import HttpResponse
from django.shortcuts import render, redirect
from .import forms

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

def connectCard(request):
    if request.method == 'POST':
        form = forms.CreateConnectCard(request.POST)
        if form.is_valid():
            #save article to db
            form.save()
    else:
        form = forms.CreateConnectCard()
    return render(request, "ifgfoc/connect-card.html", {'connectCard': form})