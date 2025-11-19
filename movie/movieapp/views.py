from django.shortcuts import render, redirect
from  django.views import View
from movieapp.forms import Movieform
from movieapp.models import Movie



class Homepage(View):
    def get(self,request):
        m=Movie.objects.all()
        context={'movieapp':m}
        return render(request,'home.html',context)

class Addmovie(View):
    def get(self,request):
        form_instance=Movieform()
        context = {'form': form_instance}
        return render(request, 'addmovie.html', context)

    def post(self,request):
        form_instance = Movieform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, 'addmovie.html')

class Details(View):
    def get(self, request, i):
        m = Movie.objects.get(id=i)
        context = {'movie': m}
        return render(request, 'details.html', context)

class Delete(View):
    def get(self,request,i):
        m=Movie.objects.get(id=i)
        m.delete()
        return redirect('home')

class Edit(View):
    def post(self,request,i):
        m=Movie.objects.get(id=i)
        form_instance=Movieform(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()

        return redirect('home')


    def get(self, request, i):
        m=Movie.objects.get(id=i)
        form_instance=Movieform(instance=m)
        context = {'form':form_instance}
        return render(request, 'edit.html',context)

