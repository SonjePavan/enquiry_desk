from django.shortcuts import render
from . models import StudentData
# Create your views here.
def home(request):
    return render(request , 'userinfo.html')
def store(request):
    firstname=request.POST['fname']
    lastname=request.POST['lname']
    email=request.POST['email']
    mobile_number=request.POST['mobile']
    address=request.POST['add']
    course=request.POST['course']
    Student_Data=StudentData(firstname=firstname,lastname=lastname,email=email,mobile_number=mobile_number,address=address,course=course)
    Student_Data.save()
    return render(request,'userinfo.html')