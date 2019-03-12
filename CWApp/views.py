from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# index page endpoint
def index(request):
    return render(request, "CWApp/index.html")
# not being used
def index2(request):
    return render(request, "CWApp/base.html")
# about page endpoint
def aboutUs(request):
    return render(request, "CWApp/aboutUs.html")
# gallery page endpoint
def gallery(request):
    return render(request, "CWApp/gallery.html")
# contact page endpoint
def contactUs(request):
    return render(request, "CWApp/contactUs.html")
# resource page endpoint
def resources(request):
    return render(request, "CWApp/resources.html")


