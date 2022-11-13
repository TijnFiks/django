from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee, Department
# Create your views here.

def index(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    return render(
        request,
        'index.html',
        {
            'employees': employees,
            'departments': departments
        }
    )

def new_employee(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    department_id = int(request.POST['department_id'])
    if request.POST['id']:
        id = int(request.POST['id'])
        employee = Employee(id=id, first_name=first_name, last_name=last_name, department_id=department_id)
    else:
        employee = Employee(first_name=first_name, last_name=last_name, department_id=department_id)
    employee.save()
    return redirect(index)

def employee(request):
    id = request.GET['id']
    employee = Employee.objects.get(id=id)
    departments = Department.objects.all()
    return render(
        request,
        'employee.html',
        {
            'employee': employee,
            'departments': departments
        }
    )

def delete_employee(request):
    id = int(request.POST['id'])
    Employee.objects.get(id=id).delete()
    return redirect(index)

def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def new_department(request):
    id = int(request.POST['id'])
    department_name = request.POST['department_name']
    department = Department(id=id, department_name=department_name)
    department.save()
    return redirect(departments)

def delete_department(request):
    id = int(request.POST['id'])
    Department.objects.get(id=id).delete()
    return redirect(departments)

def department(request):
    id = request.GET['id']
    department = Department.objects.get(id=id)
    return render(
        request,
        'department.html',
        {
            'department': department
        }
    )