
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_page, name='home'),
    path('profile/<int:user_id>', views.view_profile, name='view_profile'),
    path('courses/', include('courses.urls'), name='course_app_urls'),
    path('students/', views.view_all_students, name='view_all_students'),
    path('students/view_single_student/<int: student_id>', views.view_single_student, name='view_single_student'),
    path('students/add_new_student/', views.add_new_student, name='add_new_student'),
    path('authentication/', include('authentication.urls'), name='auth_app_urls'),
    path('payment/', include('payment.urls'), name='payment_urls'),
    path('notices/', include('notice.urls'), name='notice_urls'),
    path('library/', include('library.urls'), name='library_urls'),

    path("__reload__/", include("django_browser_reload.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
