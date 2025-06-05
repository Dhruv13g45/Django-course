from django.shortcuts import render,redirect
from students.models import Student
from .models import Courses


def assign_course_to_student(request, student_id,course_id):
    if request.method == 'POST':
        try:
            std_obj = Student.objects.get(std_roll = student_id)
            course_obj = Courses.objects.get(course_code=course_id)
            
            if std_obj and course_id:
                std_obj.std_course.set([course_obj])
        except Exception as e:
            print("An error occured ", e)
    else:
        std_rolls = [student.std_roll for student in Student.objects.all()]
        return render(request, 'assign_course_form.html', {'std_rolls' :std_rolls})
    
    return redirect('display_all_students')


def add_courses(request):
    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_desc = request.POST.get('course_desc')
        if course_title:
            Courses.objects.get_or_create(course_title = course_title, course_desc = course_desc)
            return redirect('display_all_students')
    else:
        return render(request,"add_course.html")


def associated_course_students(request,course_id):
    course = Courses.objects.get(course_code=course_id)
    students = Student.objects.filter(std_course = course)

    return render(request,'associated_course_students.html',{'students':students})
