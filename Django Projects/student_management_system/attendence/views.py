from django.utils import timezone
from django.shortcuts import render
from .models import Attendence, Courses,Student

# Create your views here.

def mark_attendence_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Courses.objects.get(course_code = course_id)

        course_students_ids = request.POST.getlist('course_students')
        

        for std_id in course_students_ids:
            attenence_status = request.POST.get(f'status_{std_id}')
            student  = Student.objects.getlist(std_roll = std_id) 
        
        Attendence.objects.update_or_create(
            student = student,
            course = course,
            attendence_date = timezone.now().date(),
            defaults= {'attendence_status' : attenence_status}
        )
        
    else:
        courses = Courses.objects.all()
        students = Student.objects.all()
    
    return render(request, 'mark_attendence.html', {'courses':courses, 'students':students})



def view_attendence_report(request):
    students_attendence = Attendence.objects.all()

    return render(request, 'view_attendence.html', {'students_attendnce': students_attendence})