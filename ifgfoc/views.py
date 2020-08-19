from django.http import HttpResponse
from django.shortcuts import render, redirect
from .import forms

# Create your views here.
def handler404(request, exception):
    return render(request, 'ifgfoc/404.html', status=404)

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

def connectcard(request):
    if request.method == 'POST':
        form = forms.CreateConnectCard(request.POST)
        if form.is_valid():
            #save forms to db
            form.save()
            return redirect('ifgfoc:index')
    else:
        form = forms.CreateConnectCard()
    return render(request, "ifgfoc/connect-card.html", {'connectCard': form})

def prayercard(request):
    if request.method == 'POST':
        form = forms.CreatePrayerCard(request.POST)
        if form.is_valid():
            #save forms to db
            form.save()
            return redirect('ifgfoc:index')
    else:
        form = forms.CreatePrayerCard()
    return render(request, "ifgfoc/prayer-card.html", {'prayerCard': form})