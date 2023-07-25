from django.urls import path
from .views import *

urlpatterns=[
    
    path('student_login_signup/',student_login_signup),
    path('student_available_exams/',student_available_exams),
    path('student_exam_instructions/',student_exam_instructions),
    path('student_exam_page/',student_exam_page),
    path('student_result/',student_result),
    path('student_result_analysis/',student_result_analysis),
    path('teacher_login_signup/',teacher_login_signup),
    path('teacher_signup/',teacher_signup),
    path('teacher_login/',teacher_login),
    path('save_student/',save_student),
    path('save_teacher/',save_teacher),
    path('student_signup/',student_signup),
    path('student_login/',student_login),
    path('logout/',logout),
    path('student_login_validation/',student_login_validation),
    path('teacher_login_validation/',teacher_login_validation),
    path('student_create_session/',student_create_session),
    path('teacher_create_session/',teacher_create_session),

    
    path('view_questions/',view_questions),
    path('save_questions/',save_questions),
    path('edit_question/',editQuestion),
    path('edit_save_question/',editSaveQuestion),
    path('edit_question/',editQuestion),
    path('delete_question',deleteQuestion),
    path('delete_question/',deleteQuestion),
    
    path('teacher_students_list/',teacher_students_list),
    path('teacher_courses_list/',teacher_courses_list),
    path('teacher_add_courses/',teacher_add_courses),
    path('teacher_add_questions/',teacher_add_questions),
    path('teacher_after_login/',teacher_after_login),
    path('save_course/',save_course),
    path('student_after_login/',student_after_login)
]
