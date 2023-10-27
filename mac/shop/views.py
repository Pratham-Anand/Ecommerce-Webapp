from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

# Create your views here.

def index(request):
    products=Product.objects.all()
    print(products)
    # n=len(products)
    # nSlides=n//4+ ceil((n/4)-(n//4))
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    params={"allProds":allProds}
    return render(request,"shop/index.html",params)
    # return HttpResponse("This is shop index")

def about(request):
    # return render(request,)
    return render(request,"shop/about.html")
    # return HttpResponse("About")

def contact(request):
    # return render(request,)
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print(name)
       
    return render(request,"shop/contact.html")
    # return HttpResponse("Contact")

def search(request):
    # return render(request,)
    return render(request,"shop/search.html")
    # return HttpResponse("search")


def tracker(request):
    # return render(request,)
     return render(request,"shop/tracker.html")
    # return HttpResponse("tracker")


def productview(request,myid):
    # return render(request,)
    product=Product.objects.filter(id=myid)
    return render(request,"shop/productview.html",{'product':product[0]})
    # return HttpResponse("productview")


def checkout(request):
    return render(request,"shop/checkout.html")
    # return HttpResponse("checkout")


