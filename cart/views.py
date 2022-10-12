from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cart_details(request,tot=0,count=0,cart_item=None):

    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_item=item.objects.filter(cart=ct,active=True)
        for i in ct_item:
            tot +=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_item,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
        return ct_id

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))

    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_item=item.objects.get(prodt=prod,cart=ct)
        if c_item.quan < c_item.prodt.stock:
            c_item.quan+=1
        c_item.save()
    except item.DoesNotExist:
        c_item=item.objects.create(prodt=prod,quan=1,cart=ct)
        c_item.save()
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_item=item.objects.get(prodt=prod,cart=ct)
    if c_item.quan>1:
        c_item.quan-=1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cartDetails')
def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_item = item.objects.get(prodt=prod, cart=ct)
    c_item.delete()
    return redirect('cartDetails')



