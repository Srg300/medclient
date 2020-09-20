from django.urls import path, include
from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout, name='logout'),

    path('patients/', views.view_pacients_list, name = 'view_pacients_list'),
    path('patient/<str:id>/', views.view_single_pacient, name = 'view_single_pacient'),
    path('patient/create/patient/', views.view_add_patient, name='view_add_patient' ),

    path('recepi/<str:id>/', views.view_single_recepi, name = 'view_single_recepi'),
    path('patient/r/recepis/', views.view_recepi_patient, name = 'view_recepi_patient'),
    
    path('doctors/', views.view_doctors_list, name = 'view_doctors_list'),
    path('doctor/<str:id>/', views.view_single_doctor, name = 'view_single_doctor'),
    path('doctor/create/doctor', views.view_add_doctor, name = 'view_add_doctor'),

    path('pill/create/', views.view_pill_create, name = 'view_pill_create'),
    path('pills/', views.view_pills_list, name = 'view_pills_list'),

    path('create/user', views.view_add_admin, name = 'view_add_admin'),
]
