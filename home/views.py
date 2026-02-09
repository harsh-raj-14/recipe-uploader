from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse as hp
def index(request):
    peoples=[
       {'name':'harsh','age':21,'salary':20000},
       {'name':'raj','age':20,'salary':26000},
       {'name':'sahil','age':19,'salary':40000},
       {'name':'ram','age':23,'salary':30000},
       {'name':'gita','age':22,'salary':35000}
    ]
    for people in peoples:
        print(people)
    return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
    print("*"*10)
    return hp("<h1>you are on success page</h1>")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")