from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"shop/index.html")
    # return HttpResponse("This is shop index")

def about(request):
    # return render(request,)
    return render(request,"shop/about.html")
    # return HttpResponse("About")

def contact(request):
    # return render(request,)
    return HttpResponse("Contact")

def search(request):
    # return render(request,)
    return HttpResponse("search")


def tracker(request):
    # return render(request,)
    return HttpResponse("tracker")


def productview(request):
    # return render(request,)
    return HttpResponse("productview")


def checkout(request):
    return HttpResponse("checkout")


