from django.shortcuts import render,redirect
from .models import Category

# Create your views here.
def category(request):
    if request.method=='GET':
        return render(request,'category.html')
    else:
        t=request.POST['categorytitle']
        cat = category(title = t)
        cat.save()
        return redirect('category')
