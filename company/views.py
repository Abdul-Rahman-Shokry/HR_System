from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch, Department


# Create your views here.

def branches(request):
    branches = Branch.objects.all()
    context={'branches':branches}
    return render(request, 'company/branches.html', context)


def branchDetails(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    departments = branch.departmentsBranch.all()
    context = {'branch':branch, 'departments':departments} 
    return render(request, 'company/branchDetails.html', context)
