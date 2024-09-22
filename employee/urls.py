from django.urls import path
from .views import EmployeesList

urlpatterns = [
    path('employees/',  EmployeesList.as_view(), name='employees'),
]
