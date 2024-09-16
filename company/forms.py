from django import forms
from .models import Department

class newDepartmentToBranchForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']


    # def clean(self):
    #     cleaned_data = self.cleaned_data

    #     try:
    #         Department.objects.get(name=cleaned_data['name'], branch_id=self.branch_id)
    #     except Department.DoesNotExist:
    #         pass
    #     else:
    #         raise forms.ValidationError('Deprtment name is already exists in this branch')

    #     # Always return cleaned_data
    #     return cleaned_data