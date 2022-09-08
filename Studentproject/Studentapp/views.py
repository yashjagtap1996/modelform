import re
from django.shortcuts import render,redirect

from Studentapp.forms import StudentForm

# Create your views here.

def registration(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    form=StudentForm()
    template_name="index.html"
    context={'form':form}
    return render(request,template_name,context)

def success(request):
    template_name='success.html'
    return render(request,template_name)