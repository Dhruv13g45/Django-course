
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from college_management_system.courses.models import Course
from users.models import StudentProfile

def welcome_page(request):
    return render(request, 'welcome.html')


def view_profile(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'profile.html', {'user_info' : user})


def view_all_students(request):
    all_students = StudentProfile.objects.all()
    return render(request,'AllStudents.html', {'all_students' : all_students})


def view_single_student(request, student_id):
    single_student = get_object_or_404(StudentProfile, pk=student_id)
    if request.method == 'POST':
        single_student.delete()
        return redirect('view_all_students')

    return render(request, 'profile.html', {'single_student' : single_student})


def add_new_student(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm_password')
        user_role = request.POST.get('user_role')

        if user_password == user_confirm_password:
            new_student = StudentProfile.objects.create(
                user_name = user_name,
                user_email = user_email,
                user_password = user_password,
                user_confirm_password = user_confirm_password,
                user_role = user_role
            )
            return redirect('profile', {'new_stduent_profile' : new_student})
        else:
            message = messages.error(request, 'Password and confirm password should be same!')
            return render(request,'addNewStudent.html', {'message' : message})
    else:
        return render(request, 'addNewStudent.html')



def assign_course_student(request, student_id, course_id):
    ## in href add like this <a href="{% url 'name' %}?param1={{ param1 }}&param2={{ param2 }}">click me</a>
    student  = get_object_or_404(StudentProfile, pk=student_id)
    course = get_object_or_404(Course, pk = course_id)
    student.student_courses.add(course)
    message = messages.success(request,'Course Assgined successfully')

    return redirect('view_all_students')