from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import userform, info, menuform


# Create your views here.

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password') 
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, "owner/login.html", {
                "message": "invalid credentials"
            })
    return render(request, "owner/login.html")

@login_required(login_url='login')
@admin_only
def main(request):
    return render(request, "owner/main.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_member(request):
    register = False
    if request.method == 'POST':
        user_form= userform(data=request.POST)
        info_form= info(data=request.POST)
        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = info_form.save(commit=False)
            profile.user = user
            profile.save()
            register = True
        else:
            return HttpResponse("<h1>somthing went wrong</h1>")
    else:
        user_form = userform(data=request.POST)
        info_form = info(data=request.POST)
        

    return render(request, "owner/add_member.html", {
        'user_form' : user_form,
        'info_form' : info_form,
        'register' : register,
    })
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pay_history(request):
    return render(request, "owner/history.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def menu(request):
    menu = Menu.objects.all()
    return render(request, "owner/menu.html",{'menu': menu})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member(request):
    user_data = user.objects.all()
    return render(request, "owner/Members.html", {
        'data' : user_data
    })



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
     return render(request, "owner/main.html")

def logout(request):
    django_logout(request)
    return redirect("login")
@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def index(request):
    return render(request, 'owner/index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def menu2(request):
    menu = Menu.objects.all()
    return render(request, "owner/menu2.html",{'menu': menu}) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def about_us(request):
    return render(request, 'owner/about_us.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def feedback(request):
    return render(request, 'owner/feedback.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pay_history(request):
    return render(request, 'owner/pay_history.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def feedback2(request):
    return render(request, 'owner/feedback2.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def pay_history2(request):
    return render(request, 'owner/pay_history2.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def about_us2(request):
    return render(request, 'owner/about_us2.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
     return render(request, "owner/main.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def home2(request):
     return render(request, "owner/index.html")



#This function will add new menu
def add_menu(request):
    if request.method == 'POST':
         form=menuform(request.POST)
         if form.is_valid():
             form.save()
             return redirect("/menu")
    else:
         form=menuform()
    return render(request,"owner/add_menu.html",{'form':form})


#This function update menu
def update_menu(request,id):
    form={}
    if request.method == 'POST':
        pi = Menu.objects.get(pk=id)
        form=menuform(request.POST, instance=pi)
        
        
        if form.is_valid():
             form.save()
             return redirect("/menu")
        else:
            pi = Menu.objects.get(pk=id)
            form=menuform(instance=pi)
    return render(request, "owner/update_menu.html",{'form':form})  

#This function delete menu
def delete_menu(request,id):
    if request.method =='POST':
        pi=Menu.objects.get(pk=id)
        pi.delete()
    menu = Menu.objects.all()

    return render(request, "owner/menu.html",{'menu': menu})

def search(request):
    query=request.GET['query']
    values=user.objects.filter(pk=query)
   
    return render(request, "owner/search.html", {
        'data': values
    })



