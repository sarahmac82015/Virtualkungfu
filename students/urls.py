from django.urls import path
from . import views

urlpatterns = [
    #localhost800/students = empty string
    path('', views.dashboard),
    path('index_s', views.index_s),
    path('dashboard', views.dashboard),
    path('createtf', views.createtf),
    path('createfl', views.createfl),
    path('newtf', views.newtf),
    path('newfl', views.newfl),
    path('<int:tested_form_id>/edit_tf_page', views.edit_tf_page),
    path('<int:formLearning_id>/edit_fl_page', views.edit_fl_page),
    path('<int:tested_form_id>/updatetf', views.updatetf),
    path('<int:formLearning_id>/updatefl', views.updatefl),
    path('<int:tested_form_id>/delete_tf', views.delete_tf),
    path('<int:formLearning_id>/delete_fl', views.delete_fl),
    path('<int:tested_form_id>/details_tf_page', views.details_tf_page),
    path('<int:formLearning_id>/details_fl_page', views.details_fl_page),
]

