from django.shortcuts import render
from .models import Contact,AI,JAVA
from .models import SE,PD,IME,DM
from .models import DS,NS,SD
from django.http import HttpResponse
# from django.Http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        iname=request.POST.get('inputname',"")
        iemail=request.POST.get('inputemail',"")
        imessage=request.POST.get('inputmessage',"")
        c=Contact(
            name=iname,
            email=iemail,
            message=imessage,
        )
        c.save()
        messages.success(request,"Message Sent Successfully")
    return render(request,'index.html')

def ai(request):
    contents=AI.objects.all()
    dictionary={'contents':contents}

    return render(request,'AI.html',dictionary)

def java(request):
    contents=JAVA.objects.all()
    dictionary={'contents':contents}
    return render(request,'JAVA.html',dictionary)

def dm(request):
    contents=DM.objects.all()
    dictionary={'contents':contents}

    return render(request,'DM.html',dictionary)

def pd(request):
    contents=PD.objects.all()
    dictionary={'contents':contents}
    return render(request,'PD.html',dictionary)

def se(request):
    contents=SE.objects.all()
    dictionary={'contents':contents}
    return render(request,'SE.html',dictionary)

def ime(request):
    contents=IME.objects.all()
    dictionary={'contents':contents}
    return render(request,'IME.html',dictionary)

def ds(request):
    contents=DS.objects.all()
    dictionary={'contents':contents}
    return render(request,'DS.html',dictionary)

def sd(request):
    contents=SD.objects.all()
    dictionary={'contents':contents}
    return render(request,'SD.html',dictionary)

def ns(request):
    contents=NS.objects.all()
    dictionary={'contents':contents}
    return render(request,'NS.html',dictionary)

    



     

