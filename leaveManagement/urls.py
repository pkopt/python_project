from django.conf.urls import url

from .views import employeeApi,getEmployee,LeaveApply



urlpatterns = [


    url(r'^qikpod/employee/add', employeeApi.as_view()),
url(r'^qikpod/employee/leave', LeaveApply.as_view()),
url(r'^qikpod/employee/getemployee', getEmployee.as_view())

    ]