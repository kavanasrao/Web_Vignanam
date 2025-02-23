from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.form import SignupForm,SigninForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
    
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            email=form.cleaned_data['email']    
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name is exists')
                return redirect('signup')
             
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('signup')
            
            else :
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                messages.info(request,'User created successfully!')
                return redirect('signin')
        
        else :
            messages.error(request,'Please correct the errors below')
            return redirect('signup')
            
    
    else:
        form = SignupForm()
   
    return render(request,'signup.html',{'form':form})
    
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('feed')
            
            else :
                messages.error(request,'Invalid credentials')
                return redirect('signin')
        else :
            messages.error(request,'Please correct the error below')
            
            
    else :
        form = SigninForm
        
    return render(request, 'signin.html',{'form':form})


@login_required
def logout_view(request):
    logout(request)  
    return redirect('home')
    
                