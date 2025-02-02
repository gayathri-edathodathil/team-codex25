from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import auth
from .models import CustomUser as User
from .models import tracker,expenses
from django.contrib import messages
from .utils import get_plot

# Create your views here.

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='' or password=='':
            messages.info(request,'All fields are required')
            return redirect('login')
        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,'Username or Password invalid')
                return redirect('login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        # repass=request.POST['retype-password']
        if username=='' or password=='' or email=='' or first_name=='':
            messages.info(request,'All fields are required')
            return redirect('signup')
        # if password!=repass:
        #     messages.info(request,'Passwords are not matching')
        #     return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already used by another account')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email,phone_number=phone)
            user.save()
            user = auth.authenticate(username=username,password=password)
            auth.login(request,user)
            return redirect('dashboard')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    next_url = request.GET.get('next','/')
    return redirect(next_url)

def dashboard(request):
    exp = expenses.objects.filter(user=request.user).first()
    pg=tracker.objects.filter(user=request.user)
    x= [x.date for x in pg]
    y= [y.amount for y in pg]
    chart = get_plot(x,y)
    return render(request,'dashboard.html',{'chart':chart,'exp':exp})

def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')

def budget(request):
    return render(request,'budget.html')