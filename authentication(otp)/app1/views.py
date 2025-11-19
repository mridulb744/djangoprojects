from django.shortcuts import render, redirect
from django.views import View
from app1.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from app1.models import Customuser


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html', context)

    def post(self,request):
        form_instance = Signupform(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()# calls generate_otp defined in model
            send_mail(
                "Django Auth OTP",
                u.otp,
                "abhiappuzz666@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('verify')

class Userlogin(View):
    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)

    def post(self,request):
        form_instance = Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)

            if user and user.is_superuser==True:
                login(request,user)
                return redirect('adminhome')
            elif user and user.role=="student":
                login(request, user)
                return redirect('studenthome')
            elif user and user.role=="teacher":
                login(request, user)
                return redirect('teacherhome')
            else:
                messages.error(request, "invalid user credentials")
                return redirect('login')

class Userlogout(View):
    def get(self,request):
      logout(request)
      return redirect('login')


class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')


class Otp_verify(View):
    def get(self,request):
        return render(request,'verify.html')

    def post(self,request):
        o=request.POST['o']
        u=Customuser.objects.get(otp=o)
        u.is_active=True
        u.is_verified=True
        u.otp=None
        u.save()
        return  redirect('login')