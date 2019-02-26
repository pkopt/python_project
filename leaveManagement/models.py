from django.db import models

# Create your models here.


class Employee(models.Model):

    MANAGER = 'MGR'
    STANDARD = 'STD'
    EMPLOYEE_TYPES = (

        (MANAGER, 'manager'),
        (STANDARD, 'employee')

    )
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    name = models.CharField(max_length=100, null=True, blank=True)
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    manager = models.ForeignKey('self', null=True, related_name='employee',on_delete=models.CASCADE)

    def __repr__(self):
        return self.__str__()


class leave(models.Model):
    leave_choices = (
        ('s', 'sick'),
        ('c', 'casual'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    employee_id=models.CharField(max_length=100, null=True, blank=True)
    Dateofleave = models.CharField(max_length=50, null=True, blank=True)
    typeofleave = models.CharField(max_length=1, choices=leave_choices, default='NA')

