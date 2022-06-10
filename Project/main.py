users = {'Charlie': '12345',
         'Steve': 'apple',
         'Kate': '0000',
         'Mary': 'python'
         }


def decorator(func):
    def wrapper(name, password):
        if not check_password(name, password):
            print("Не правильное Имя или Пароль")
            return False
        return func

    return wrapper


@decorator
def login(name, password):
    return True


def check_password(name, password):
    return users.get(name) == password


if __name__ == "__main__":
    n = 3
    while n > 0:
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
