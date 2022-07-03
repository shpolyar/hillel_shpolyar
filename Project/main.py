import argparse
import json
import sys
from datetime import timedelta, datetime


class UserDoesNotExist(Exception):
    pass


def read_file(file_name):
    try:
        with open(file_name) as f:
            return json.load(f)
    except OSError as e:
        print(e)


def write_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False)
    except OSError as e:
        print(e)


def check_password(name, password):
    users = read_file('data.json')
    if users.get(name) is not None:
        if not users.get(name).get('password') == password:
            raise UserDoesNotExist("Неверный Пароль")
        else:
            return True
    else:
        raise UserDoesNotExist("Данного имени не существует")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help=' Your username')
    parser.add_argument('--password', help='Your password')
    return parser.parse_args()


def is_block(name):
    users = read_file('data.json')
    r = datetime.now() - datetime.strptime(users[name]['last_try'], "%Y-%m-%d %H:%M")
    if r < timedelta(minutes=5):
        print(f"Вы заблокированы! Следующая попытка через {timedelta(minutes=5) - r} мин")
        sys.exit()
    return True


def last_try(name):
    try:
        d = read_file('data.json')
        d[name]['last_try'] = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        write_file('data.json', d)
    except KeyError:
        pass


def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            check_password(name, password)
        except UserDoesNotExist as e:
            print(e)
            return False
        if not is_block(name):
            return False
        return func(*args, **kwargs)

    return wrapper


@decorator
def login(name, password):
    return True


if __name__ == "__main__":
    n = 3
    if parse().name is None:
        name = input("Введите Имя: ")
    else:
        name = parse().name

    if parse().password is None:
        password = input("Введите Пароль: ")
    else:
        password = parse().password

    while n > 0:
        if n < 3:
            name = input("Введите Имя: ")
            password = input("Введите Пароль: ")
        if login(name, password):
            print("Вы в системе!")
            break
        n -= 1
        if n:
            print(f"У вас осталось попыток: {n}")
        else:
            print("Попытки истекли!")
            last_try(name)
