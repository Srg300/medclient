import re
import requests
import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Pacients
from django.http import JsonResponse
from .forms import Drug
from django.http import HttpResponseRedirect, HttpResponse
from .utils import *


# Обработка  главной страницы index.html
def index(request):
    try:
        user = get_curetn_user(request)
        context={
            'user': user,
        }
        return render(request, 'index.html', context=context)
    except:
        return render(request, 'login.html', )

def login(request):
    user = get_curetn_user(request)
    context={
        'user': user,
    }
    return render(request, 'login.html', context=context)


def auth(request):
    try:
        token = jwt_request(request)
        if not request.COOKIES.get('token'):
            response = render(request, 'success_login.html')
            response.set_cookie('token', token)
            return response
        else:
            return render(request, 'login.html', )
    except:
        return render(request, 'error_message.html')


def logout(request):
    if request.COOKIES.get('token'):
        response = render(request, 'login.html')
        response.delete_cookie('token')
        return response 
    else:
        response = render(request, 'login.html')
        return response 


def view_add_patient(request):
    """ Добовляем пациентов """
    user = get_curetn_user(request)
    if user.get('is_is_superuser') == True:
        doctors = get_doctors_list(request)
    else:
        doctors = get_doctors_list(request)
    context={
        'doctors': doctors,
        'user': user
    }
    return render(request, 'patient_add.html', context=context)


def view_pacients_list(request):
    """Отображаем список больных"""
    user = get_curetn_user(request)
    try:
        patients = get_patients_list(request) 
        context = {
            'patients':patients,
            'user': user
        }
        return render(request, 'patients_list.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_single_pacient(request, id):
    """отображаем данные больного"""
    user = get_curetn_user(request)
    users = get_users_list(request)
    doctors = get_doctors_list(request)
    pills = get_pills_list(request)['results']
    try:
        patient = get_patien_detail(request, id)
        context = {
            'patient':patient,
            'users':users,
            'doctors':doctors,
            'pills': pills,
            'user': user,
        }
        return render(request, 'single_patient.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_single_recepi(request, id):
    """Отображаем данные рецепта"""
    user = get_curetn_user(request)
    pills = get_pills_list(request)['results']
    try:
        recepi = get_recepi_detail(request, id)     
        context = {
            'recepi':recepi,
            'pills':pills,
            'user': user,
        }        
        return render(request, 'single_recepi.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_pills(request, id):
    """Отображаем данные рецепта"""
    user = get_curetn_user(request)
    pills = get_pills_list(request)['results']
    try:
        context = {
            'pills':pills,
            'user': user,
        }        
        return render(request, 'single_recepi.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_pill_create(request):
    user = get_curetn_user(request)
    context={
        'user': user
    }
    return render(request, 'pill_create.html', context=context)


def view_add_doctor(request):
    user = get_curetn_user(request)
    context={
        'user': user,
    }
    return render(request, 'doctor_create.html', context=context)


def view_doctors_list(request):
    """отображаем данные больного"""
    user = get_curetn_user(request)
    try:
        doctors = get_doctors_list(request)
        context = {
            'doctors':doctors,
            'user': user,
        }
        return render(request, 'doctors_list.html', context=context)
    except:
        return render(request, 'error_message.html')


def view_single_doctor(request, id):
    """отображаем данные доктора"""
    user = get_curetn_user(request)
    users = get_users_list(request)
    try:
        doctor = get_doctor_detail(request, id)
        context = {
            'doctor':doctor,
            'users':users,
            'user': user,
        }
        return render(request, 'single_doctor.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_pills_list(request):
    """отображаем список всех лекарств"""
    user = get_curetn_user(request)
    try:
        pills = get_pills_list(request)['results'] 

        context = {
            'pills':pills,
            'user': user, 
        }
        return render(request, 'pills_list.html', context=context)
    except:
        # return HttpResponse('no access', content_type='text/plain')
        return render(request, 'error_message.html')


def view_recepi_patient(request):
    user = get_curetn_user(request)
    
    recepis = get_recepi_list(request)['results']
    context = {
        'recepis': recepis,
        'user': user,
    }
    return render(request, 'recepis_patient.html' ,context=context)


def view_add_admin(request):
    user = get_curetn_user(request)
    context={
        'user': user,
    }
    return render(request, 'user_create.html', context=context)