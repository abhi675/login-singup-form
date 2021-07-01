from django.core.checks import messages
from django.shortcuts import redirect, render
from . models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(username=username,password=password).exists():
            user=User.objects.get(username=username,password=password)
            subject='Welcome back'.format(user.firstname)
            message='You have successfully login into our page with your username {}, Thank You'.format(user.username)
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email,from_email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            global account
            account=user
            return render(request,'home.html',{'user':user})

        else:
            messages.error(request,'Invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')

def signup(request):

    if request.method=='GET':  
        return render(request,'signup.html')

    elif request.method=='POST' and 'image' in request.FILES:
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        number=request.POST.get('number')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        image=request.FILES['image']
        
        if password1!=password2:
            messages.error(request,'Given passwords are not same')
            return render(request,'signup.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username is already taken')
            return render(request,'signup.html')

        elif User.objects.filter(email=email).exists():
            messages.error(request,'email is already taken')
            return render(request,'signup.html')
        
        user=User(username=username,firstname=firstname,lastname=lastname,password=password1,email=email,number=number,image=image)
        user.save()
        subject='Thank you for your response'
        message='Welcome to Page {}, We got your mail from {}, You have successfully signup into our page, Thank You'.format(firstname,email)
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)


        messages.success(request,'You have successfully signup into our page, Please login this time')
        return redirect('login')

   
    else:
        messages.error(request,'Please upload the image')
        return render(request,'signup.html')



def logout(request):
    
    return redirect('login')

def modify(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password1')
        email=request.POST.get('email')
        number=request.POST.get('number')
        
        account.firstname=firstname
        account.lastname=lastname
        account.email=email
        account.number=number
        account.username=username
        account.password=password
        if 'image' in request.FILES:
            account.image=request.FILES['image']
       
        account.save()
        subject='Thank you for your response'
        message='Your profile has been updated {} {} with {} having {}and number is {}, Thank You'.format(firstname,lastname,email,username,number)
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        user=account
        return render(request,'home.html',{'user':user})
    return render(request,'modify.html',{'account':account})