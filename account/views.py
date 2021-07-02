from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import contacts

def register(request):
    if request.method == "POST":
     first_name=request.POST['first_name']
     last_name=request.POST['last_name']
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     password2=request.POST['password2']
     
     
     if password == password2:
         if User.objects.filter(username=username).exists():
             messages.error(request,'Username taken')
             return redirect('register')
         else:
             if User.objects.filter(email=email).exists():
                messages.error(request,'email taken') 
                return redirect('index')
             else:
                 user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                 user.save();
                 messages.success(request,'You are registered and can login')
                 return redirect('login')
                
     else:
         messages.error(request,'password not match')
         return redirect('register')
    else:
        return render(request,'account/register.html')   

def login(request):
     if request.method == "POST":
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           messages.success(request,'You are logged in!')
           return redirect('dashboard')
       else:
            messages.error(request,'Invalid user')
            return redirect('login')
     else:
       return render(request,'account/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'Successfully logged out')
        return redirect('index')



def dashboard(request):
    user_contacts=contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts,
    }
    return render(request,'account/dashboard.html',context)
