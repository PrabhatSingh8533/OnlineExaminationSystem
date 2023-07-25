import time
from django.shortcuts import render
from exam.models import Student, Teacher
from exam.models import Question, Course
from django.http import HttpResponseRedirect, HttpResponse
import random
from datetime import date, datetime

# ---------------------------------------------------COMMON-------------------------------------------------------------------------------------------------------------------------------------------------------------


def landingpage(request):
    res = render(request, 'exam/landing_page.html')
    return res



# ---------------------------------------------------STUDENT---------------------------------------------------------------------------------------------------------------------------------------------------------------


# >>>>>>>>>>>>>>>
def student_login_signup(request):
    res = render(request, 'exam/student_login_signup.html')
    return res


# >>>>>>>>>>>>>>>
def student_signup(request):
    d1 = {}
    try:
        if request.GET['error'] == str(1):
            d1['errmsg'] = 'Username Already Exists !!!'
    except:
        d1['errmsg'] = ''
    res = render(request, 'exam/student_signup.html', d1)
    return res


# >>>>>>>>>>>>>>>>
def student_login(request):
   
    res = render(request, 'exam/student_login.html')
    return res


def student_after_login(request):
    res = render(request, 'exam/student_after_login.html')
    return res


# >>>>>>>>>>>>>>>>
def student_login_validation(request):
    try:
        user = Student.objects.get(username=request.POST['username'],
                                   password=request.POST['password'])
        request.session['username'] = user.username
        request.session['realname'] = user.realname
        request.session['role'] = user.role
        url = "http://localhost:8000/exam/student_create_session/"
    except:
        url = "http://localhost:8000/exam/student_login/"

    return HttpResponseRedirect(url)


# >>>>>>>>>>>>>>>>>
def student_create_session(request):
    try:
        realname = request.session['realname']
    except KeyError:
        return HttpResponseRedirect(
            "http://localhost:8000/exam/student_login/")

    res = render(request, 'exam/student_after_login.html')
    return res


# >>>>>>>>>>>>>>>
def student_available_exams(request):
    course_list = list(Course.objects.all())
    res = render(request, 'exam/student_available_exams.html',
                 {'courses': course_list})
    return res


# >>>>>>>>>>>>>>>
def student_exam_instructions(request):
    course = request.GET['course']
    
    exam_date_scheduled = Course.objects.get(
        coursename=request.GET['course']).date
    exam_time_scheduled = Course.objects.get(
        coursename=request.GET['course']).scheduled_exam_time
    
   
    # if (exam_date_scheduled != date.today()):
    #     res = render(request, 'exam/student_after_login.html')
    #     return res

    request.session['course'] = request.GET['course']
    questions_pool = list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['course'])))
    total_marks = 0
    total_ques = 0
    total_time = Course.objects.get(coursename=request.GET['course']).time
    negative_marking = Course.objects.get(
        coursename=request.GET['course']).negative_marking
    for question in questions_pool:
        total_marks = total_marks + question.marks
    for question in questions_pool:
        if question.ques:
            total_ques += 1
            
    section_quesA_pool=list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['course']),section='A'))
    section_A_ques=0
    for question in section_quesA_pool:
     if question.ques:
        section_A_ques+=1
    section_quesB_pool=list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['course']),section='B'))
    section_B_ques=0
    for question in section_quesB_pool:
     if question.ques:
        section_B_ques+=1        
    d = {
        'totalmarks': total_marks,
        'totalques': total_ques,
        'totaltime': total_time,
        'sectionA_no':section_A_ques,'sectionB_no':section_B_ques,
        'negative_marking': negative_marking,
        'exam_time_scheduled':exam_time_scheduled
    }
    res = render(request, 'exam/student_exam_instructions.html', d)
    return res


# >>>>>>>>>>>>>>>
def student_exam_page(request):
    course_name = request.GET['examname']
   
    total_time = Course.objects.get(coursename=request.GET['examname']).time
    
    
    
    
    no_of_que_section_A=int(request.GET.get('sectionAtotalque'))
    questions_pool_section_A=list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['examname']), section ='A'))
    random.shuffle(questions_pool_section_A)
    questions_list_section_A=questions_pool_section_A[:no_of_que_section_A]
   
    no_of_que_section_B=int(request.GET.get('sectionBtotalque'))
    questions_pool_section_B=list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['examname']), section ='B'))
    random.shuffle(questions_pool_section_B)
    questions_list_section_B=questions_pool_section_B[:no_of_que_section_B]
    
    
    
    res = render(
        request, 'exam/student_exam_page.html', {
            'questions_list_section_A':questions_list_section_A,'questions_list_section_B':questions_list_section_B,
            'totaltime': total_time,
            'course_name': course_name
        })
    return res


# >>>>>>>>>>>>>>>>
def student_result(request):
  
    total_questions = Question.objects.filter(course=Course.objects.get(
        coursename=request.GET['course'])).count()
    
    total_marks=0
    questions_pool = list(Question.objects.filter(course=Course.objects.get(coursename=request.GET['course'])))
    for question in questions_pool:
        total_marks = total_marks + question.marks

    total_attempt = 0
    total_right = 0
    total_wrong = 0
    total_negative_marks = 0
    total_positive_marks = 0
    

    qno_list = []
    for k in request.POST:
        if k.startswith("qno"):
            qno_list.append(int(request.POST[k]))
    for n in qno_list:
        question = Question.objects.get(qnos=n)
        negative_marks_for_question = question.negative_marks
        try:
            if question.answer == request.POST['q' + str(n)]:
                total_right += 1
                total_positive_marks = total_positive_marks + (question.marks)
            else:
                total_wrong += 1
                total_negative_marks = total_negative_marks + (
                    negative_marks_for_question)
            total_attempt += 1
        except:
            pass

    marks_obtained = total_positive_marks - total_negative_marks
    unattempted = total_questions - total_attempt
    d = {
        'total_attempt': total_attempt,
        'total_right': total_right,
        'total_wrong': total_wrong,
        'marks_obtained': marks_obtained,
        'total_questions': total_questions,
        'unattempted': unattempted,
        'total_marks' : total_marks
    }
    res = render(request, 'exam/student_result_analysis.html', d)
    return res




# >>>>>>>>>>>>>>>>
def save_student(request):
    user = Student()
    u = Student.objects.filter(username=request.POST['username'])
    if not u:
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.realname = request.POST['realname']
        user.role = "LEARNER"
        user.save()
        url = "http://localhost:8000/exam/student_login/"
    else:
        url = "http://localhost:8000/exam/student_signup?error=1"
    return HttpResponseRedirect(url)





# >>>>>>>>>>>>>>>>
def logout(request):

    request.session.clear()
    url = "http://localhost:8000/"
    return HttpResponseRedirect(url)


# >>>>>>>>>>>>>>>>>
def student_result_analysis(request):
    res = render(request, 'exam/student_result_analysis.html')
    return res


# ------------------------------------------------TEACHER---------------------------------------------------------------------------------------------------------------------------------------------------------------


def teacher_login_signup(request):
    res = render(request, 'exam/teacher_login_signup.html')
    return res


def teacher_signup(request):
    d1 = {}
    try:
        if request.GET['error'] == str(1):
            d1['errmsg'] = 'Username Already Exists !!!'
    except:
        d1['errmsg'] = ''
    res = render(request, 'exam/teacher_signup.html', d1)
    return res


def teacher_login(request):
  
    res = render(request, 'exam/teacher_login.html')
    return res


def teacher_after_login(request):

    res = render(request, 'exam/teacher_after_login.html')
    return res


def teacher_login_validation(request):
    try:
        user = Teacher.objects.get(username=request.POST['username'],
                                   password=request.POST['password'])
        request.session['username'] = user.username
        request.session['realname'] = user.realname
        request.session['role'] = user.role
        url = "http://localhost:8000/exam/teacher_create_session/"
    except:
        url = "http://localhost:8000/exam/teacher_login/"

    return HttpResponseRedirect(url)


# >>>>>>>>>>>>>>>>>>>
def teacher_create_session(request):
    try:
        realname = request.session['realname']
    except KeyError:
        return HttpResponseRedirect(
            "http://localhost:8000/exam/teacher_login/")

    res = render(request, 'exam/teacher_after_login.html')
    return res


# >>>>>>>>>>>>>>>>>>>
def save_teacher(request):
    user = Teacher()
    u = Teacher.objects.filter(username=request.POST['username'])
    if not u:
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.realname = request.POST['realname']
        user.role = "TEACHER"
        user.save()
        url = "http://localhost:8000/exam/teacher_login/"
    else:
        url = "http://localhost:8000/exam/teacher_signup?error=1"
    return HttpResponseRedirect(url)


# >>>>>>>>>>>>>>>>>>>>>
def teacher_students_list(request):
    students = Student.objects.all()
    res = render(request, 'exam/teacher_students_list.html',
                 {'students': students})
    return res


# >>>>>>>>>>>>>>>>>>>>>
def teacher_courses_list(request):
    courses = Course.objects.all()
    res = render(request, 'exam/teacher_courses_list.html',
                 {'courses': courses})
    return res


# >>>>>>>>>>>>>>>>>>>>>
def teacher_add_courses(request):
    res = render(request, 'exam/teacher_add_courses.html')
    return res


# >>>>>>>>>>>>>>>>>>>>>>
def teacher_add_questions(request):
    res = render(request, 'exam/teacher_add_questions.html')
    return res


# >>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>
def save_course(request):
    course = Course()
    course.coursename = request.POST.get('coursename')
    course.time = request.POST.get('time')
    course.negative_marking = request.POST.get('negative_marking')
    course.date = request.POST.get('date')
    course.scheduled_exam_time = request.POST.get('scheduled_exam_time')
    request.session['coursename'] = request.POST.get('coursename')
    course.save()
    return HttpResponseRedirect(
        'http://localhost:8000/exam/teacher_add_questions/')



# --------------------------------------TEST RELATED----------------------------------------------------------------------------------------------------------------------------------------------------------



def save_questions(request):

    coursename = Course.objects.get(coursename=request.POST['coursename'])
    course_negative_marking = coursename.negative_marking

    question = Question()

    marks = request.POST['marksassigned']

    question.ques = request.POST['question']
    question.optA = request.POST['optiona']
    question.optB = request.POST['optionb']
    question.optC = request.POST['optionc']
    question.optD = request.POST['optiond']
    question.answer = request.POST['answer']
    
    question.marks = marks
    question.section=request.POST['section']
   

    question.negative_marks = (course_negative_marking) * int(marks)

    question.course = coursename
    question.save()
    url = 'http://localhost:8000/exam/view_questions/'
    return HttpResponseRedirect(url)


def view_questions(request):
    questions = Question.objects.all()
    res = render(request, 'exam/view_questions.html/',
                 {'questions': questions})
    return res


def editQuestion(request):
    q = request.GET['qno']
    question = Question.objects.get(qnos=int(q))
    res = render(request, 'exam/edit_question.html', {'question': question})
    return res


def editSaveQuestion(request):
    
    question = Question.objects.get(qnos=int(request.POST['qno']))
    question.qnos = request.POST['qno']
    question.ques = request.POST['question']
    question.optA = request.POST['optiona']
    question.optB = request.POST['optionb']
    question.optC = request.POST['optionc']
    question.optD = request.POST['optiond']
    question.answer = request.POST['answer']
    question.marks = request.POST['marksassigned']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/exam/view_questions/')


def deleteQuestion(request):
    q = request.GET['qno']
    question = Question.objects.get(qnos=int(q))
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/exam/view_questions/')
