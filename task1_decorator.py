class PermissionError(Exception):
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f'PermissionError: Access denied for user "{self.user}"'


permitted_role = ['admin']


def check_access(role):
    def inner(func):
        def wrapper():
            if role not in permitted_role:
                raise PermissionError(role)
            return func()
        return wrapper
    return inner


@check_access('admin')
def user_login():
    return "Добро пожаловать!"


print(user_login())
# Результат работы: Добро пожаловать!


@check_access('user')
def user_login():
    return "Добро пожаловать!"


print(user_login())
# Результат работы: PermissionError: Access denied for user "user"
