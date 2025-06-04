from django.shortcuts import render, get_objects_or_404
from .models import Student


def display_students(request):
    if request.method == "GET":
        students = Student.objects.all()

    return render(request, 'displayAllStudents.html', {'all_students': students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get('student_name')
        course = request.POST.get('student_course')
        email = request.POST.get('student_email')
        single_student_obj = Student.objects.create(std_name=name,std_email=email,std_course=course)
    
    return render(request,'addStudent.html',{'single_student' : single_student_obj})



def edit_student_profile(request,student_id):
    if request.method == "POST":
        std_obj = get_objects_or_404(Student,student_id)
        name = request.POST.get('student_name')
        email = request.POST.get('student_email')
