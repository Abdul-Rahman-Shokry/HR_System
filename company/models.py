from django.db import models

# Create your models here.
# 1:13:29
class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, help_text="enter full address")
    phone = models.CharField(max_length=12, null = True)
    email = models.EmailField(max_length=50, null = True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, help_text="write a description about the department")
    branch = models.ForeignKey('Branch', related_name="branch", on_delete=models.CASCADE)

    def __str__(self):
        return self.name