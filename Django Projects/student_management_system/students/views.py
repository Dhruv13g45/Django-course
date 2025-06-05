
from django.shortcuts import render, get_object_or_404,redirect

from courses.models import Courses
from .models import Student


def display_students(request):
    if request.method == "GET":
        students = Student.objects.all()

    return render(request, 'displayAllStudents.html', {'all_students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        email = request.POST.get('student_email')
        password = request.POST.get('student_password')

        std_obj = Student.objects.create(std_name= name , std_email = email, std_password = password)
    
    return render(request,'add_student.html',{'std_profile' : std_obj})


def edit_student_profile(request,student_id):
    if request.method == "POST":
        std_obj = get_object_or_404(Student,student_id)
        name = request.POST.get('student_name')
        email = request.POST.get('student_email')

        std_obj.std_name = name
        std_obj.std_email = email

        std_obj.save()

    return render(request,'edit_profile.html',{'std_obj':std_obj})


def view_single_student(request,student_id):
    std_obj = get_object_or_404(Student,student_id)
    return render(request,"view_profile.html",{'std_obj':std_obj})


def delete_student_profile(request,student_id):
    if request.method == 'POST':
        std_obj = get_object_or_404(Student,student_id)
        std_obj.delete()
        return redirect('all_students')