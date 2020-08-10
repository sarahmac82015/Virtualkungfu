from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard', views.dashboard),
    path('new', views.new),
    path('createtf', views.createtf),
    path('createfl', views.createfl),
    path('<int:tested_form_id>/edit_tf', views.edit_tf),
    path('<int:formlearning_id>/edit_fl', views.edit_fl),
    path('<int:tested_form_id>/updatetf', views.updatetf),
    path('<int:formLearning_id>/updatefl', views.updatefl),
    path('<int:tested_form_id>/delete_tf', views.delete_tf),
    path('<int:formLearning_id>/delete_fl', views.delete_fl),
    path('<int:tested_form_id>/details_tf', views.details_tf),
    path('<int:formLearning_id>/details_fl', views.details_fl),
]