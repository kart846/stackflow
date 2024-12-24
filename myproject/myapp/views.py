from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
# Create your views here.
def hom(request):
     return render(
        request,
        "app/home.html",
        # {
        #     "foo": "bar",
        # },
        # content_type="application/xhtml+xml",
    )
login_required    
def signuppage(request):
     form=Register()
     if request.method == 'POST':
         form=Register(request.POST)
         if form.is_valid():
             form.save()
             return redirect('myapp:login')
     return render(request,'forms/signup.html',{'form':form})
        
# def loginpage(request):
#     form=Signin()
#     if request.method == 'POST':
#         form = Signin(request,data=request.POST)
#         if form.is_valid():
#             user = authenticate(username = form.cleaned_data['username'],password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request,user)
#                 return redirect('home')
    
#     return render(request, 'forms/login.html', {'form':form})

# def signout(request):
#     logout(request)
#     return redirect('stackbase:home')
#     return render(request, 'forms/logout.html',)
def signout(request):
    logout(request)
    return render(request, 'forms/logout.html')

login_required
def profile(request):
    return render(request, 'forms/profile.html')

@login_required
def profile_update(request):
    
    if request.method == "POST":
       u_form = UserUpdateForm(request.POST,instance=request.user)
       p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile )
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Account Updated Sucessfully')
           return redirect('myapp:profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)   
    context = {
      'u_form':u_form,
      'p_form':p_form
    
    }
    return render(request, 'forms/profile_update.html', context)



   
