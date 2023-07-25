from django.db import models


class Course(models.Model):
    coursename = models.CharField(max_length=20)
    time = models.IntegerField(default=1)
    negative_marking = models.FloatField()
    date = models.DateField()
    scheduled_exam_time=models.TimeField()

    def __str__(self):
        return self.coursename


class Question(models.Model):
    qnos = models.IntegerField(primary_key=True, auto_created=True)
    ques = models.CharField(max_length=140, default='oes')
    optA = models.CharField(max_length=40, default='oes')
    optB = models.CharField(max_length=40, default='oes')
    optC = models.CharField(max_length=40, default='oes')
    optD = models.CharField(max_length=40, default='oes')
    answer = models.CharField(max_length=1, default='oes')
    marks = models.FloatField(default=1)
    section= models.CharField(max_length=20,default='A')
    negative_marks = models.FloatField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    # def __str__(self):
    #  return self.qnos


class Student(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    realname = models.CharField(max_length=20)

    def __str__(self):
        return self.realname


class Teacher(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    realname = models.CharField(max_length=20)

    def __str__(self):
        return self.realname
