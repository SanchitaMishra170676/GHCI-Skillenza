# This is made by team AAshray {@Vanshika, @Sakshi, @Sachita}


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def login1(request):
    return render(request, 'F1signin.html')

def login2(request):
    return render(request, 'F2signin.html')

def login4(request):
    return render(request, 'F4signin.html')

def login5(request):
    return render(request, 'F5signin.html')

def login7(request):
    return render(request, 'F7signin.html')

def login8(request):
    return render(request, 'F8signin.html')

def feedback(request):
    return render(request, 'feedback.html')

def volRegistration(request):
    return render(request, 'volunteer-registration.html')

def needVolReg(request):
    return render(request,'needvol-regestration.html')

def ShopReg(request):
    return render(request,'shop-registration.html')

def CustReg(request):
    return render(request,'order-regestration.html')

def PlasmaReg(request):
    return render(request,'plasma-registration.html')

def NeedPlasmaReg(request):
    return render(request,'needplasma-regestration.html')

def volunteer(request):
    user = request.GET.get('uid', 'default')
    params = {
        'uname': user
    }
    return render(request,'volunteer-page.html',params)

def needvolunteer(request):
    return render(request,'needvol-page.html')

def pre(request):
    return render(request,'precautionary-page.html')

def shop(request):
    return render(request,'Regshop-page.html')

def orderpage(request):
    return render(request,'order-page.html')

def anti(request):
    return render(request,'anti-dep-page.html')

def donor(request):
    return render(request,'donor-page.html')

def needplasma(request):
    return render(request,'needplasma-page.html')

def about(request):
    return render(request,'about-us.html')