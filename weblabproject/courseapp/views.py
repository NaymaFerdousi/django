from django.shortcuts import render, redirect

from .models import Course
from .forms import CourseForm
# Create your views here.
def home(request):
    all_courses= Course.objects.all()
    return render(request,'courseapp\index.html',{'courses':all_courses})

def rem(request,id):
    c = Course.objects.get(id=id)
    c.delete()
    return redirect(home)

def addNew(request):
    frm=CourseForm()
    return render(request, 'courseapp/addnew.html',{'cform':frm})

# def save(request):
#     if request.method=="POST":
#         form=CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect(home)

def save(request):
    if request.method=="POST":
        frm=CourseForm(request.POST)
        if frm.is_valid():
            try:
                frm.save()
                return redirect(home)
            except:
                pass
    return redirect(home) 

def edit(request,id):
    course = Course.objects.get(id=id)
    frm=CourseForm(instance=course)
    return render(request,'courseapp/edit.html', {'form': frm})

def update(request,id):
    course = Course.objects.get(id=id)
    form = Course(request.POST,isinstance=course)
    if form.is_valid():
        form.save()
        return redirect(home)
    return redirect(home)