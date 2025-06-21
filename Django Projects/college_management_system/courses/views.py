from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from .models import Course

# Create your views here.
def view_all_courses(request):
    all_courses = Course.objects.all()
    return render(request,'AllCourses.html', {'all_courses' : all_courses})


def add_new_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_start_date = request.POST.get('course_start_date')
        course_end_date = request.POST.get('course_end_date')
        course_fees = request.POST.get('course_fees')
        course_intake = request.POST.get('course_intake')

        new_course = Course.objects.create(
            course_name = course_name,
            course_start_date = course_start_date,
            course_end_date = course_end_date,
            course_name = course_name,
            course_fees = course_fees,
            course_intake = course_intake,
        )

        new_course.save()
        message = messages.success(request,'Course added successfully!')
        return redirect('all_courses')
    else:
        return render(request, 'AddCourses.html')

def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course,pk=course_id)
        course.delete()
        return redirect('all_courses')
    else:
        return render(request, 'AllCourses.html')
