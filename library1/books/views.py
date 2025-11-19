from django.shortcuts import render,redirect
from django.template.defaultfilters import title
from django.views import View
from books.forms import Addbooksform
from books.models import Book

# def home(request):
#     return render(request,'home.html')
#
# def viewbooks(request):
#     return render(request,'viewbooks.html')

# def addbooks(request):
#     return render(request,'addbooks.html')


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Viewbooks(View):
    def get(self, request):
        b=Book.objects.all()
        context={'books':b}
        return render(request, 'viewbooks.html',context)


class Addbooks(View):
    def get(self,request):
        form_instance=Addbooksform()
        context = {'form': form_instance}
        return render(request, 'addbooks.html', context)

    def post(self,request):
        form_instance = Addbooksform(request.POST,request.FILES)
        if form_instance.is_valid():
            # data = form_instance.cleaned_data
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
            # b.save()
            form_instance.save()
        return render(request, 'addbooks.html')

class Details(View):
        def get(self,request,i):
            print(i)
            b=Book.objects.get(id=i)
            context={'book':b}
            return render(request,'details.html',context)

class Delete(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')





class Edit(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance = Addbooksform(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:viewbooks')

    def get(self, request, i):
        b=Book.objects.get(id=i)
        form_instance=Addbooksform(instance=b)
        context = {'form':form_instance}
        return render(request, 'edit.html', context)




