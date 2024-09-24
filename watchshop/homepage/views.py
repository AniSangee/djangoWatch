from django.shortcuts import render, redirect
from .models import Watches, WatcheUpload
from .forms import uploadform
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    watches= WatcheUpload.objects.all()
    context= {'watch': watches}
    return render(request,'home.html',context)

def About(request):
    return render(request,'about.html')

@login_required(login_url="/login")
def upload(request):
    if request.method == 'POST':
        form = uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = uploadform()
    
    return render(request,'watchUpload.html',{'form':form})

# loginpage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =authenticate(username = username, password = password) 
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form})
    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

# signup
def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
         form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404
def ShowProduct(request, id):
    product = get_object_or_404(WatcheUpload, id=id)
    return render(request,'product.html',{'product':product})
