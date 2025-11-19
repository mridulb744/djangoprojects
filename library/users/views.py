from django.shortcuts import render,redirect
from django.views import View
from users.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


class Register(View):
    def post(self,request):
        form_instance = Signupform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')



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

            if user:
                login(request,user)
                return redirect('books:home')
            else:
                messages.error(request, "Invalid User Credentials")
                return redirect('users:login')



    def get(self,request):
        form_instance=Loginform()
        context={'form':form_instance}
        return render(request,'login.html',context)

class Userlogout(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')



