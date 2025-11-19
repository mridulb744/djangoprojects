from django.shortcuts import render
from django.views import View
from app1.forms import Additionform,Factorialform,Bmiform,Signupform

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Addition(View):
    def get(self,request):
        form_instance=Additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)

    def post(self,request):


        #creating form object using submitted data
        form_instance=Additionform(request.POST)
        #checks wether the data is valid or not
        if form_instance.is_valid():
            #process the data after validation
            data=form_instance.cleaned_data
            print(data)

            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            print(s)
            context={'result':s,'form':form_instance}
            return render(request,'addition.html',context)






class Factorial(View):
    def get(self,request):
        form_instance=Factorialform()
        context = {'form': form_instance}
        return render(request,'factorial.html',context)


    def post(self,request):
        form_instance = Factorialform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)

            n=data['num']
            fact=1
            for i in range(1,n+1):
                fact *=i
                print(fact)

            context={'result':fact,'form':form_instance}


            return render(request, 'factorial.html',context)




class Bmi(View):
    def get(self,request):
        form_instance = Bmiform()
        context = {'form': form_instance}
        return render(request,'bmi.html',context)



    def post(self,request):
        form_instance = Bmiform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            w=data['weight']
            h=data['height']/100
            bmi=w/(h**2)
            print(bmi)
            context={'result':bmi,'form':form_instance}

            return render(request, 'bmi.html',context)





class Signup(View):

    def get(self,request):
        form_instance = Signupform()
        context = {'form': form_instance}
        return render(request, 'signup.html', context)

