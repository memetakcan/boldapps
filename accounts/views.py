from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("home")
    return render(request,"accounts/form.html",{"form":form, "title":"Login"})

def logout_view(request):
    logout(request)
    return redirect("home")