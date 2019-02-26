from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .searlizer import EmployeeSearilizer,leaveSearilizer
from .models import Employee
from .dateFinder import dateFinder
# Create your views here.

class employeeApi(APIView):
    def post(self, request, format=None):
        serializer = EmployeeSearilizer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response({"Sucess": "Employee save Successfilly"})

        return Response(serializer.errors)





class LeaveApply(APIView):
    def post(self, request, format=None):

        employeeId = request.data['employee_id']
        leavedate= request.data['Dateofleave']






        try:

            employee = Employee.objects.get(employee_id=employeeId)
            boolvalue = dateFinder(leavedate)
            if boolvalue is True:
                return Response({"Holiday": "this day is come under national Holiday"})
            else:
                serializer = leaveSearilizer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)


        except Employee.DoesNotExist:
            return Response({"error":"user does not exist"})





class getEmployee(APIView):
    def post(self, request):
        managerID=request.data['manager']
        role_id= request.data['role']


        employee = Employee.objects.filter(manager=managerID, role=role_id)
        print("pankaj")
        serializer = EmployeeSearilizer(employee,many=True)
        return Response(serializer.data)








