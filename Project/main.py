import argparse
import time
from datetime import timedelta, datetime

wrong_try = datetime(2022, 6, 22, 16, 20)
now = datetime(2022, 6, 22, 16, 24, 55)

users = {'Charlie': '12345',
         'Steve': 'apple',
         'Kate': '0000',
         'Mary': 'python'
         }


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help=' Your username')
    parser.add_argument('--password', help='Your password')
    return parser.parse_args()


def blocking(t1, t2, n):
    r = t2 - t1
    if r < timedelta(minutes=5) and n - 1 == 0:
        print("Попытки истекли!")
        print(f"Вы заблокированы! Следующая попытка через {timedelta(minutes=5) - r} мин")
        time.sleep(timedelta.total_seconds(timedelta(minutes=5) - r))
        return False
    return True


def decorator_name(func):
    def wrapper(*args, **kwargs):
        if not check_password(name, password):
            print("Не правильное Имя или Пароль")
            return False
        return func(*args, **kwargs)

    return wrapper


def decorator_time(func):
    def wrapper(*args, **kwargs):
        if not blocking(wrong_try, now, n):
            return False
        return func(*args, **kwargs)

    return wrapper


@decorator_name
@decorator_time
def login(name, password, wrong_try, now, n):
    return True


def check_password(name, password):
    return users.get(name) == password


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
        if login(name, password, wrong_try, now, n):
            print("Вы в системе!")
            break
        n -= 1
        if n:
            print(f"У вас осталось попыток: {n}")
