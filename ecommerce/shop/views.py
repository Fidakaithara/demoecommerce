from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from shop.models import Category
from shop.models import Product
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate

# Create your views here.


def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,"categories.html",context)


def products(request,p):
    c=Category.objects.get(id=p)  #reads a particular category object using id
    p=Product.objects.filter(category=c)  #read all the products under a particular category object
    context={'cat':c,'pro':p}
    return render(request,"products.html",context)


def productsdetails(request,p):
    p=Product.objects.get(id=p)
    context={'pro':p}
    return render(request,"productdetails.html",context)




def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if (p == cp):
            u = User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:login')


def addcategories(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        c = Category.objects.create(name=n, image=i, description=d)
        c.save()
        return redirect('shop:categories')

    return render(request, "addcategories.html")


def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES['i']
        p = request.POST['p']
        s = request.POST['s']
        c = request.POST['c']
        cat=Category.objects.get(name=c)
        p = Product.objects.create(name=n, description=d,image=i,price=p,stock=s,category=cat)
        p.save()
        return redirect('shop:categories')
    return render(request, "addproducts.html")



def addstock(request,i):
    p=Product.objects.get(id=i)

    if(request.method=="POST"): # After form submission
        p.stock=request.POST['n']
        p.save()
        return redirect('shop:productdetails',i)

    context={'pro':p}
    return render(request, "addstock.html",context)

