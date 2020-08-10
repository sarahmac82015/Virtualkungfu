from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000 -> views.index
    path('', views.index),
    # localhost:8000/create -> views.create
    path('create', views.create),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('<int:user_id>', views.show)
]