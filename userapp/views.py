from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegistrationForm 
from .forms import *
from .models import *

def register_Farm(request):
    if request.method=='POST':
        form=FarmForm(request.POST) #Farm is class name in forms.py
        if form.is_valid():
            form.save()
            return redirect('Farm_list') #Redirect to book list page
    else:
        form = FarmForm()
    return render(request, 'register_Farm.html', {'form': form})
def Farm_list(request):
    Farms = Farm.objects.all() #Farm is class name in models.py
    return render(request, 'Farm_list.html',{'Farms':Farms}) 

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data["email"]
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('index')
        else:
           form = RegistrationForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    if request.method =='post':
        form = AuthenticationForm(request,data=request.post)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'user_login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('index')




def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def product(request):
    return render(request,'product.html')
def service(request):
    return render(request,'service.html')
def blog(request):
    return render(request,'blog.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def feature(request):
    return render(request,'feature.html')
def login(request):
   return render(request,'login.html')
def logout(request):
   return render(request,'logout.html')
def detail(request):
    return render(request,'detail.html')
def register(request):
   return render(request,'register.html')
def register_Farm(request):
   return render(request,'register_Farm.html')
def contact(request):
  return render(request,'contact.html') 


