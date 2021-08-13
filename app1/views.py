from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Person

# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method == 'POST':
        if request.POST.get('first_name'):
            person = Person()
            person.first_name=request.POST.get('first_name')
            person.save()  
    person=Person.objects.all()

    context = {"person":person}
    return render(request,'register.html',context)


    return render(request,"register.html")
def dash(request):
    return render(request,"index.html")
