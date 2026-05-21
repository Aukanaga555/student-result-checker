from django.shortcuts import render
from.models import Student

def add_student(request):
    if request.method=='POST':
        name=request.POST['name']
        roll_number=request.POST['roll_number']
        dob=request.POST['dob']
        mark=request.POST['mark']

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            dob=dob,
            mark=mark
        )
        return redirect('search')
    return render(request,'add_student.html')

def search_result(request):
    if request.method=='POST':
        roll_number=request.POST['roll_number'] 
        student=Student.objects.get(roll_number=roll_number)
        return render(request,'result.html',{'student':student})   
