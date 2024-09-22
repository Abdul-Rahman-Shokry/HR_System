from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    salary = models.IntegerField(max_length=6)
    birth_date = models.DateField()
    # national_id = models.IntegerField()
    position_id = models.ForeignKey('Position',related_name='position_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(max_length=2)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name