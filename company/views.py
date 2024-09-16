from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponse
from .models import Branch, Department
from django.shortcuts import get_object_or_404 # ??
from .forms import newDepartmentToBranchForm



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
    

def newBranch(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branchName')
        branch_address = request.POST.get('branchAddress')
        branch_phone = request.POST.get('branchPhone')
        branch_email = request.POST.get('branchEmail')
        
        try:
            branch = Branch(
                name=branch_name,
                address=branch_address,
                phone=branch_phone,
                email=branch_email
            )
            branch.save()
            messages.success(request, 'Branch created successfully!')
        except IntegrityError:
            messages.error(request, 'Branch name already exists. Please choose a different name.')
        
        return redirect('newBranch')  
    return render(request, 'company/newBranch.html')


def editBranch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    
    if request.method == 'POST':
        branch_name = request.POST.get('branchName')
        branch_address = request.POST.get('branchAddress')
        branch_phone = request.POST.get('branchPhone')
        branch_email = request.POST.get('branchEmail')

        try:
            branch.name = branch_name
            branch.address = branch_address
            branch.phone = branch_phone
            branch.email = branch_email
            branch.save()
            messages.success(request, 'Branch updated successfully!')
            return redirect('branchesDetails', branch_id=branch_id)
        except IntegrityError:
            messages.error(request, 'Branch name already exists. Please choose a different name.')
    
    context = {'branch': branch}
    return render(request, 'company/editBranch.html', context)


def newDepartmentToBranch(request,branch_id):
    b = Branch.objects.get(pk=branch_id)
    form = newDepartmentToBranchForm()
    if request.method == 'POST':
        form = newDepartmentToBranchForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.branch_id = branch_id
            department.save()
            return render(request,'company/branchDetails.html',{'branch':b})
    return render(request,'company/newDepartmentToBranch.html',{'form':form,'branch':b})