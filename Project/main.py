import argparse
from datetime import timedelta, datetime


time = datetime(2022, 6, 22, 16, 23)

user = {'dasha': {'password': '1111', 'last_try': '2022-06-22 16:20'}}


class UserDoesNotExist(Exception):
    pass


def check_password(name, password):
    if user.get(name) is not None:
        if not user.get(name).get('password') == password:
            raise UserDoesNotExist("Не правильное Имя или Пароль")
        else:
            return True
    else:
        raise UserDoesNotExist("Не правильное Имя или Пароль")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help=' Your username')
    parser.add_argument('--password', help='Your password')
    return parser.parse_args()


def is_block(name, time_2):
    last_try = user[name]['last_try']
    r = time_2 - datetime.strptime(last_try, "%Y-%m-%d %H:%M")
    if r < timedelta(minutes=5):
        print(f"Вы заблокированы! Следующая попытка через {timedelta(minutes=5) - r} мин")
        return False
    return True


def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            check_password(name, password)
        except UserDoesNotExist as e:
            print(e)
            return False
        if not is_block(name, time):
            return False
        return func(*args, **kwargs)

    return wrapper


@decorator
def login(name, password, wrong_try, now):
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
        if login(name, password, time):
            print("Вы в системе!")
            break
        n -= 1
        if n:
            print(f"У вас осталось попыток: {n}")
        else:
            print("Попытки истекли!")
