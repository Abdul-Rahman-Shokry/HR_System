"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from company import views as CompanyViews
from employee import views as EmployeeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CompanyViews.branches, name = "branches"),
    path('branch/<int:branch_id>',CompanyViews.branchDetails,name="branchesDetails"),
    path('new_branch', CompanyViews.newBranch, name="newBranch"),
    path('branch/<int:branch_id>/edit/', CompanyViews.editBranch, name="editBranch"),
    path('branch/<int:branch_id>/newDepartment/', CompanyViews.newDepartmentToBranch, name="newDepartmentToBranch"),
    # path('',include('accounts.urls')),
    path('',include('employee.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('employees', EmployeeViews.EmployeesList.as_view(), name="employees"),
    path('new-employee', EmployeeViews.newEmployee, name="newEmployee")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
