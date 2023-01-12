from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    all_student = models.Student.objects.all()
    return render(request,'studentapp\index.html',{'students':all_student})

def rem(request,id):
    s = models.Student.objects.get(id=id)
    s.delete()
    return redirect(home)