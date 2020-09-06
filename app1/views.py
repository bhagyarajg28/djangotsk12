from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm,RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request, 'base1.html')




# def registration(request, **kwargs):
#     if request.method == "POST":
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save(commit=True)
#             return redirect(loginn)
#         else:
#             return render(request, 'register.html', {'f': f})
#     else:
#         f = UserCreationForm()
#         return render(request, 'register.html', {'f': f})


def registration(request, **kwargs):
    if request.method == "POST":
        f = RegisterForm(request.POST)
        p=ProfileForm(request.POST,request.FILES)
        if p.is_valid() and f.is_valid():
            user=f.save()
            usrprof = p.save(commit=False)
            usrprof.user=user
            usrprof.Unique_Id()
            usrprof.save()
            return redirect(loginn)
        else:
            return render(request, 'register.html', {'p':p,'f':f})
    else:

        p=ProfileForm
        f=RegisterForm
        return render(request, 'register.html', {'p':p,'f':f})


def loginn(request):
    if request.method == "POST":
        t1 = request.POST['t1']
        t2 = request.POST['t2']
        print(t1)
        print(t2)
        user = authenticate(username=t1,password=t2)
        login(request, user)
        p=Profile.objects.get(user__username=t1)
        return render(request,'profile.html',{'p':p})

            #return redirect(registration)
    else:
        return render(request, 'login.html')




# def profile(request):
#     p=Profile.objects.get(pk=5)
#     print(p.UniqueId)
#     return render(request, 'profile.html', {'p': p})


def logout_view(request):
    logout(request)
    return render(request, 'base1.html')