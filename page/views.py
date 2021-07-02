from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import price_choice,state_choice,bedroom_choice

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choice':state_choice,
        'price_choice':price_choice,
        'bedroom_choice':bedroom_choice,
    }
    return render(request,'pagelayout/index.html',context)
def about(request):
    realtor=Realtor.objects.order_by('-hire_date')
    mvp=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtor':realtor,
        'mvp':mvp,
    }
    return render(request,'pagelayout/about.html',context)

