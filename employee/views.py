from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee, Position


class EmployeesList(ListView):
    model = Employee
    template_name = 'employee/employees.html'
    context_object_name = 'employees'

def newEmployee(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        salary = request.POST['salary']
        birth_date = request.POST['birth_date']
        national_id = request.POST['national_id']
        Employee.objects.create(
            name= name,
            age= age,
            alary= salary,
            birth_date=birth_date, 
            national_id=national_id
        )
    return render(request,'employee/newEmployee.html')