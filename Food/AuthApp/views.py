from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request,'AuthApp/register.html',context)

def login_view(request):
    if request.method =="POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user=authenticate(request, username = u ,password = p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    context = {}
    return render(request,'AuthApp/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')