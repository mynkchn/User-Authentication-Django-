from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.
def home(request) :
   return render(request,'auth/home.html',{})



def register_view(request) :
    if request.method=='POST' :
      
      form=UserCreationForm(request.POST) 
      if form.is_valid() :
            print("Form is valid. Saving user...")
            user=form.save()
            return redirect('/login')
        # Debugging line to log form errors
    else :
     form=UserCreationForm()
  
    return render(request,'auth/register.html',{'form':form})

def login_view(request):
     if request.method=='POST' :
        form=AuthenticationForm(data=request.POST)
        if form.is_valid() : 
           user=form.get_user()
           login(request,user)
           return redirect('/home')
     else :
        form=AuthenticationForm()
     messages.success(request,"Incorrect Login Credentials")
     return render(request,'auth/login.html',{'form':form})     

def dashboard(request) :
   return render(request,'auth/dashboard.html',{})       

def logout(request) :
   return redirect('/home/')
