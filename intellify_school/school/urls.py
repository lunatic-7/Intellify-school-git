from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.schoolHome, name="school_home"),

    # AUTHENTICATION
    path('school-register/', views.schoolRegister, name="school_register"),
    path('school-login/', views.schoolLogin, name="school_login"),
    path('school-logout/', views.schoolLogout, name='school_logout'),
]