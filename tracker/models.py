from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class WorkEntry(models.Model):
    teacher_name = models.CharField(max_length=100)
    class_section = models.CharField(max_length=50)
    exam_name = models.CharField(max_length=100)
    subject_group = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    student_status = models.CharField(max_length=50)
    completion_percent = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.teacher_name} - {self.class_section} - {self.subject_name}"
