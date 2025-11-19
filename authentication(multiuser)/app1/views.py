from django.shortcuts import render,redirect
from django.views import View
from app1.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')


    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'register.html', context)

class Userlogin(View):
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)

            if user and user.is_superuser==True:
                login(request,user)
                return redirect('adminhome')

            elif user and user.role=="student":
                login(request,user)
                return redirect('studenthome')

            elif user and user.role=="teacher":
                login(request,user)
                return redirect('studenthome')


            else:
                messages.error(request, "Invalid User Credentials")
                return redirect('users:login')



    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)

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
