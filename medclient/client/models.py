from django.db import models
import requests


class Pacients():
    def get_pacients_list(self):
        URL = 'http://127.0.0.1:8000/api/patients/'
        TOKEN_ADMIN = '059b9562fa0f98d96bf32dc7e5721fd1445eb118'
        # response = requests.get(URL, params = {Token:'059b9562fa0f98d96bf32dc7e5721fd1445eb118'})
        response = requests.get('http://127.0.0.1:8000/api/patients/')
        data = response.json()['results'][0]
        return data

