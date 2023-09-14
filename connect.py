import requests
import json


def post_new_user(username, login, pwd, hobby, about_me):  # Загружает данные пользователя в users
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/.json"
    json_data = {login: {"pwd": pwd, "username": username, "hobby": int(hobby), "about_me": about_me}}
    requests.patch(url=db_url, json=json_data)


def get_user_by_login(login):  # Получает данные пользователя из users по логину
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/"
    res = requests.get(f"{db_url}/{login}.json").json() #Получение json-файла
    hobby = res['hobby']
    username = res['username']
    pwd = res['pwd']
    ab_me = res['about_me'] #Обо мне
    return {
        "login": login,
        "pwd": pwd,
        "username": username,
        "hobby": hobby,
        "ab_me": ab_me
    }

def delete_user_by_login(login):  # Удаляет данные из users по логину
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users/"
    requests.delete(f"{db_url}/{login}.json").json()


def create_group(gr_name, login, ab_gr="Без описания"):  # Создаёт группу с 1-м начальным пользователем (владельцем)
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/groups"
    json_data = {gr_name: {"users": {"user": login}, "ab_gr": ab_gr}}
    requests.patch(url=f"{db_url}.json", json=json_data)


def add_to_group(gr_name, login):  # Добавляет пользователя в группу
    db_url = f"https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/groups/{gr_name}/users/"
    json_data = {login: "user"}
    requests.patch(url=f"{db_url}.json", json=json_data)


def delete_group(gr_name):  # Удаляет группу
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/groups"
    requests.delete(f"{db_url}/{gr_name}.json").json()


def check_login(login: object) -> object:  # Проверяет наличие пользователя в БД
    db_url = "https://amn-project-b3b8c-default-rtdb.europe-west1.firebasedatabase.app/users"
    res = requests.get(f"{db_url}/{login}.json").json()
    return False if res == None else True