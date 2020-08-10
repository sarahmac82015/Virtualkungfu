from django.db import models
from home.models import User
from datetime import datetime
# Create your models here.

class TestedFormManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['form_name']) < 5:
            errors['form_name'] = "The form name must consist of at least 5 characters"
        if len(form_data['video_doc']) < 7:
            errors['video_doc'] = "A url must consist of at least  7 characters"
        #if test_date > datetime.today():
            #errors['test_date'] = "Test Date cannot be in the future"
        if len(form_data['test_date']) < 1:
            errors['test_date'] = "Date field required"
        if len(form_data['inst_comments']) < 5:
            errors['inst_comments'] = "Instructor comments must consist of at least 5 characters"
        if len(form_data['contd_form_goals']) < 5:
            errors['contd_form_goals'] = "Continued Form Goals must consist of at least 5 characters"
        if len(form_data['student_comments']) < 5:
            errors['student_comments'] = "Student comments must consist of at least 5 characters"
        return errors


class TestedForm(models.Model):
    form_name = models.CharField(max_length=255)
    video_doc = models.CharField(max_length=255)
    test_date = models.DateField()
    inst_comments = models.CharField(max_length=255)
    contd_form_goals = models.CharField(max_length=255)
    student_comments = models.CharField(max_length=255)
    tested_form = models.ManyToManyField(User, related_name="users_tf")
    
    objects = TestedFormManager()

class FormLManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['formName']) < 5:
            errors['formName'] = "The form name must consist of at least 5 characters"
        if len(form_data['formVideo']) < 7:
            errors['formVideo'] = "A url must consist of at least  7 characters"
        if len(form_data['formNotes']) < 5:
            errors['formNotes'] = "Form Notes must consist of at least 5 characters"
        if len(form_data['studentVideoDoc']) < 7:
            errors['studentVideoDoc'] = "A url must consist of at least  7 characters"
        if len(form_data['instComments']) < 5:
            errors['instComments'] = "Instructor comments must consist of at least 5 characters"
        if len(form_data['studentComments']) < 5:
            errors['studentComments'] = "Student comments must consist of at least 5 characters"
        return errors

class FormL(models.Model):
    formName = models.CharField(max_length=255)
    formVideo = models.CharField(max_length=255)
    formNotes = models.CharField(max_length=255)
    studentVideoDoc = models.CharField(max_length=255)
    instComments = models.CharField(max_length=255)
    studentComments = models.CharField(max_length=255)
    formLearning = models.ManyToManyField(User, related_name="users_fl")

    objects = FormLManager()