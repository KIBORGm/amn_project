import requests
import json


class User:
    def __init__(self, login, pwd, username, hobby):
        self.username = username
        self.login = login
        self.pwd = pwd
        self.hobby = hobby


def load_data(username, login, pwd, hobby):  # Загружает данные пользователя в users
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/.json"
    json_data = {login: {"pwd": pwd, "username": username, "hobby": hobby}}
    requests.patch(url=db_url, json=json_data)


def get_data(login):  # Получает данные пользователя из users по логину
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/"
    res = requests.get(f"{db_url}/{login}.json").json() #Получение json-файла
    hobby = res['hobby']
    username = res['username']
    pwd = res['pwd']


def delete_data(login):  # Удаляет данные из users по логину
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/"
    res = requests.delete(f"{db_url}/{login}.json").json()
