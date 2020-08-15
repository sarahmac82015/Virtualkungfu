from django.shortcuts import render, HttpResponse, redirect 
from .models import TestedForm, FormL
from home.models import User
from django.contrib import messages
from datetime import datetime
# Create your views here.


def index_s(request):   
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'students/dashboard.html', context)


def dashboard(request):    
    this_user = User.objects.get(id=request.session['user_id'])
    userstfs = this_user.users_tf.all()
    usersfl = this_user.users_fl.all()
    context = {
        'this_user': this_user,
        'tested_forms_mine': userstfs,
        'formLearning_mine': usersfl,
    }
    return render(request, 'students/dashboard.html', context)

def createtf(request):
    errors = TestedForm.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)

        return redirect('/students/newtf')

    newtf=TestedForm.objects.create(
        form_name=request.POST['form_name'],
        video_doc=request.POST['video_doc'],
        test_date=request.POST['test_date'],
        inst_comments=request.POST['inst_comments'],
        contd_form_goals=request.POST['contd_form_goals'],
        student_comments=request.POST['student_comments'],  
    )
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.users_tf.add(newtf)
    return redirect('/students')


def createfl(request):
    errors = FormL.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)

        return redirect('/students/newfl')

    newfl=FormL.objects.create(
        formName=request.POST['formName'],
        formVideo=request.POST['formVideo'],
        formNotes=request.POST['formNotes'],
        studentVideoDoc=request.POST['studentVideoDoc'],
        instComments=request.POST['instComments'],
        studentComments=request.POST['studentComments'],
    )
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.users_fl.add(newfl)
    return redirect('/students')

def newtf(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'students/newforms.html', context)

def newfl(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'students/newformsl.html', context)


def edit_tf_page(request, tested_form_id):
    this_user = User.objects.get(id=request.session['user_id'])
    one_tested_form = TestedForm.objects.get(id=tested_form_id)
    context = {
        'tested_form': one_tested_form,
        'this_user': this_user
    }
    return render(request, 'students/edit_tf.html', context) 
    
def edit_fl_page(request, formLearning_id):
    this_user = User.objects.get(id=request.session['user_id'])
    one_formLearning = FormL.objects.get(id=formLearning_id)
    context = { 
        'formLearning': one_formLearning,
        'this_user': this_user
    }
    return render(request, 'students/edit_fl.html', context)

def updatetf(request, tested_form_id):
    errors = TestedForm.objects.validate(request.POST)
    #if errors:
        #for e in errors.values():
            #messages.error(request, e)
    #return redirect (f'/students/{tested_form_id}/edit_tf.html')

    to_update = TestedForm.objects.get(id=tested_form_id)
    to_update.form_name = request.POST['form_name']
    to_update.video_doc = request.POST['video_doc']
    to_update.test_date = request.POST['test_date']
    to_update.inst_comments = request.POST['inst_comments']
    to_update.contd_form_goals = request.POST['contd_form_goals']
    to_update.student_comments = request.POST['student_comments']
    to_update.save()
    
    return redirect('/students')  


def updatefl(request, formLearning_id):
    print('updatefl')
    #errors = FormL.objects.validate(request.POST)
    #if errors:
        #for e in errors.values():
            #messages.error(request, e)
    #return redirect (f'/students/{formLearning_id}/edit_fl_page')

    to_update = FormL.objects.get(id=formLearning_id)
    to_update.formName = request.POST['formName']
    to_update.formVideo = request.POST['formVideo']
    to_update.formNotes = request.POST['formNotes']
    to_update.studentVideoDoc = request.POST['studentVideoDoc']
    to_update.instComments = request.POST['instComments']
    to_update.studentComments = request.POST['studentComments']
    to_update.save()
    
    return redirect('/students')

def delete_fl(request, formLearning_id):
    to_delete = FormL.objects.get(id=formLearning_id)
    to_delete.delete()
    return redirect('/students')

def delete_tf (request, tested_form_id):
    to_delete = TestedForm.objects.get(id=tested_form_id)
    to_delete.delete()
    return redirect('/students')

def details_fl_page(request, formLearning_id):
    this_user = User.objects.get(id=request.session['user_id'])
    one_formLearning = FormL.objects.get(id=formLearning_id)
    context = {
        'formLearning': one_formLearning,
        'this_user': this_user
    }
    return render(request, 'students/detailsformlearning.html', context)

def details_tf_page(request, tested_form_id):
    this_user = User.objects.get(id=request.session['user_id'])
    one_tested_form = TestedForm.objects.get(id=tested_form_id)
    context = {
        'tested_form': one_tested_form,
        'this_user': this_user
    }
    return render(request, 'students/detailstestedform.html', context)



