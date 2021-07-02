from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import  UpdateView
from .models import Employee
from .forms import EmployeeForm

def index(request):
    employees = Employee.objects.all()
    return render(request,'main.html',{'employees':employees})

def get_employee(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            form.save()
            # redirect to a new URL:
            return redirect('/service')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()

    return render(request, 'create.html', {'form': form})

def edit(request,id):
    # if this is a POST request we need to process the form data
    obj = get_object_or_404(Employee,pk=id)
    form = EmployeeForm(request.POST or None,instance = obj)

        # create a form instance and populate it with data from the request:
        # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        print(form.cleaned_data)
        form.save()
        # redirect to a new URL:
        return redirect('/service')
    else:
        print(form.has_error) 
    return render(request, 'edit.html', {'form': form})

def delete(request,id):
    obj = get_object_or_404(Employee,pk=id)
    if not obj is None:
        obj.delete() 
    return redirect('/service')