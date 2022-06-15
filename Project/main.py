import argparse

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


def decorator(func):
    def wrapper(*args, **kwargs):
        if not check_password(name, password):
            print("Не правильное Имя или Пароль")
            return False
        return func(*args, **kwargs)
    return wrapper


@decorator
def login(name, password):
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
    # чувствую, что предыдущих два if надо бы заменить функцией, но не придумала как ее написать

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
