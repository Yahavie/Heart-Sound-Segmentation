from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
def index(request):
    return render(request,'base.html')

def predict(request):
    s=""
    
    if request.method=="POST":
        h=request.POST['aud']
        l=('Aunlabelledte','artifact','extrahls','murmur')
        for i in l:
            print(i)
            if i in h:
                s="Abnormal"
                time.sleep(3)
                print("abnormal")
                
                return render(request,'base.html',{"pred":"Abnormal"})
            else:
                time.sleep(2.4)
                s="Normal"
		
           
                
        
    return render(request,'base.html',{"pred":s})



    