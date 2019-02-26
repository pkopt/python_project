from rest_framework import serializers
from .models import Employee,leave

class EmployeeSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee


        fields = ('id','role','name','employee_id','manager')


class leaveSearilizer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields = ('id','name','employee_id','Dateofleave','typeofleave',)






