from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from django.contrib.auth.models import Group, User

# Create your views here.


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
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
    user_form = CreateUserForm(request.POST)
    info_form = info(request.POST)
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        info_form = info(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            form1 = user_form.save()
            group3 = Group.objects.get(name='member')
            form1.groups.add(group3)
            mb = info_form.data['Mobile']
            dp = info_form.data['department']
            pm = info_form.data['Pay_mode']
            tm = info_form.data['Time_mode']
            user.objects.create(
                user_id=form1, Mobile=mb, department=dp, Pay_mode=pm, Time_mode=tm)
            register = True

    else:
        user_form = CreateUserForm(request.POST)
        info_form = info(request.POST)

    return render(request, "owner/add_member.html", {
        'user_form': user_form,
        'info_form': info_form,
        'register': register,
    })


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pay_history(request):
    return render(request, "owner/history.html")


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def menu(request):
    menu = Menu.objects.all()
    return render(request, "owner/menu.html", {'menu': menu})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member(request):
    user_data = User.objects.all()
    '''for i in user_data:
        for j in i:
            print(j)
            reff = i.id
            a=user.objects.get(user_id=reff)
            mobile=a.Mobile
            department=a.Department
            pay=a.Pay_mode
            time=a.Time_mode'''
    return render(request, "owner/Members.html", {
        'data': user_data })



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
    return render(request, "owner/menu2.html", {'menu': menu})


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
def pay_history(request,pk):
    total=0
    a=[]
    member = User.objects.get(pk=pk)
    type(member)
    values = Transaction.objects.filter(
         Member_id__username__icontains=member,
        )
    b = Payment.objects.filter(
         Member_id__username__icontains=member,
        )
    for i in b:
        adv=i.Amount_paid
       
    for i in values:
        total=total+i.Amount

    due=total-deu
    if due<=0:
        advance=-due
        due=0
        st='Paid'
    else:
        advance=0
        st='Due'
    return render(request, 'owner/pay_history.html', {'total':total,'member':member,'due':due,'st':st,'advance':advance})


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


# This function will add new menu
def add_menu(request):
    if request.method == 'POST':
        form = menuform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/menu")
    else:
        form = menuform()
    return render(request, "owner/add_menu.html", {'form': form})


# This function update menu
def update_menu(request, id):
    form = {}
    if request.method == 'POST':
        pi = Menu.objects.get(pk=id)
        form = menuform(request.POST, instance=pi)

        if form.is_valid():
             form.save()
             return redirect("/menu")
        else:
            pi = Menu.objects.get(pk=id)
            form = menuform(instance=pi)
    return render(request, "owner/update_menu.html", {'form': form})

# This function delete menu


def delete_menu(request, id):
    if request.method == 'POST':
        pi = Menu.objects.get(pk=id)
        pi.delete()
    menu = Menu.objects.all()

    return render(request, "owner/menu.html", {'menu': menu})


def search(request):
    query = request.GET['query']
    values = User.objects.filter(
        username__icontains=query,
        )
   
    for i in values:
        reff = i.id
        a=user.objects.get(user_id=reff)
        mobile=a.Mobile
        department=a.Department
        pay=a.Pay_mode
        time=a.Time_mode

    return render(request, "owner/search.html", {
        'data': values,'mobile':mobile,'department':department,'pay':pay,'time':time
    })
    





def add_transaction(request, pk):
    a=dict()
    if request.method == 'POST':
        form = transactionform(request.POST)
        if form.is_valid():
            form = transactionform(request.POST)
            member = User.objects.get(pk=pk)

            mn = int(form.data['Menu1_id'])
            mns = Menu.objects.get(Menu_id=mn)
            m=str(mns)
            qt = form.data['Quantity']
            qtr=int(qt)
            b=Menu.objects.all()
            
           
            for i in b:
                a[i.Name]=i.Price
            
            if m in a.keys():
                prc=a[m]*qtr
            pd = request.POST.get('Paid')
            if pd == 'on':
                pd = True
            else:
                pd = False
           
            Transaction.objects.create(Member_id=member, Menu1_id=mns, Quantity=qt,Amount=prc, Paid=pd)
            # return redirect("add_transaction")
    else:
        form = transactionform()
    return render(request, "owner/add_transaction.html",{
        'form': form,'pk':pk
    })
    

def notcome(request):
    notcome = Absent.objects.all()
    return render(request, "owner/notcome.html", {'notcome': notcome})


def absent(request):
    if request.method == 'POST':
        form = absentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home2")
    else:
        form = absentform()
    return render(request, "owner/absent.html", {'form': form})


#userprofile
def userprofile(request):
    fm = {}
    if request.method == 'POST':
        fm = EditUserProfileForm(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
            return redirect("/userprofile")

    else:
        fm = EditUserProfileForm(instance=request.user)
    return render(request, "owner/userprofile.html", {'form': fm})

def add_payment(request, pk):
    if request.method == 'POST':
        form = paymentform(request.POST)
        if form.is_valid():
            form = paymentform(request.POST)
            member = User.objects.get(pk=pk)
            mns=form.data['Amount_paid']
            Payment.objects.create(Member_id=member, Amount_paid=mns)
            # return redirect("add_transaction")
    else:
        form = paymentform()
    return render(request, "owner/add_payment.html",{
        'form': form,'pk':pk
    })

def more(request,pk):
    total=0
    a=[]
    member = User.objects.get(pk=pk)
    type(member)
    values = Transaction.objects.filter(
         Member_id__username__icontains=member,
        )
    b = Payment.objects.filter(
         Member_id__username__icontains=member,
        )
    for i in values:
        total=total+i.Amount

    return render(request, "owner/more.html",{
        'values':values,'total':total,'b':b
    })