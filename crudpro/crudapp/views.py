from django.shortcuts import render,redirect
from .models import EmpData
from django.http import HttpResponse


def homeviews(request):
    emp = EmpData.objects.all()
    return render(request,'homepage.html',{'emps':emp})

def addemp(request):
    if request.method == 'GET':
        return render(request,'empdata.html')
    else:
        EmpData(
            first_name = request.POST['fname'],
            middle_name =  request.POST['mname'],
            last_name =  request.POST['lname'],
            email =  request.POST['email'],
            contact =  request.POST['contact'],
            company =  request.POST['company'],
            salary =  request.POST['salary'],
            location =  request.POST['location'],
        ).save()

        return redirect(homeviews)

def update(request, id):
    emp = EmpData.objects.get(id=id)
    return render(request,'updatingemp.html',{'emp':emp})

def updating_emp(request, id):
    emp = EmpData.objects.get(id=id)
    emp.first_name = request.POST['fname']
    emp.middle_name = request.POST['mname']
    emp.last_name = request.POST['lname']
    emp.email = request.POST['email']
    emp.contact = request.POST['contact']
    emp.company = request.POST['company']
    emp.salary = request.POST['salary']
    emp.location = request.POST['location']
    emp.save()
    return redirect(homeviews)

def delete(request, id):
    emp = EmpData.objects.get(id=id)
    emp.delete()
    return redirect(homeviews)