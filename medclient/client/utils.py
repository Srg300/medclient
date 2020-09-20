import requests
import json



def jwt_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    url = "http://127.0.0.1:8000/api/token/"
    data = {
        'username': username,
        'password': password,
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    token_acces = response.json()['access']
    return token_acces


def get_curetn_user(request):
    """Получаем список всех пользователей"""
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/users/me', headers=params)
    user = response.json()
    return user


def get_users_list(request):
    """Получаем список всех пользователей"""
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/users/', headers=params)
    users = response.json()['results']
    return users


def get_patien_detail(request, id):
    """Получаем данные больного"""
    id = str(id)
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/patient/' + id, headers=params)
    patient = response.json()
    return patient


def get_patients_list(request):
    """Получаем список всех пациентов"""
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/patients/', headers=params)
    patients = response.json()['results']
    return patients


def get_pills_list(request):
    """Получаем список лекарств"""
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/pills/', headers=params)
    pills = response.json()
    return pills


def get_pill_detail(request, id):
    """Получаем данные лекарства"""
    id = str(id)
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/pill/' + id, headers=params)
    pill = response.json()
    return pill


def get_doctors_list(request):
    """Получаем список всех докторов"""
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/doctors/', headers=params)
    doctors = response.json()['results']
    return doctors


def get_doctor_detail(request, id):
    """Получаем данные доктора"""
    id = str(id)
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/doctor/' + id, headers=params)
    doctor = response.json()
    return doctor


def get_recepi_list(request):
    """Получаем список рецептов """
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/recepis/', headers=params)
    recepis = response.json()
    return recepis   


def get_recepi_detail(request, id):
    """Получаем данные рецепта"""
    id = str(id)
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.get('http://127.0.0.1:8000/api/recepi/' + id, headers=params)
    recepi = response.json()
    return recepi


def update_recepi_detail(request, id):
    id = str(id)
    access_token = request.COOKIES['token']
    params = {'Authorization': 'JWT ' + access_token, 'Content-Type': 'application/json'}
    response = requests.put('http://127.0.0.1:8000/api/recepi/' + id, headers=params)
    recepi = response.json()
    return recepi
