import re
import time


class LoginCheck:
    def _check_length(self, login):
        if not login:
            return 'Вы не ввели логин'
        if len(login) > 20:
            return 'Вы ввели слишком длинный логин'
        return True

    def check_with_built_in(self, login):
        status = self._check_length(login)
        if status is True:
            return status
        return status

    def check_with_prepared_sets(self, login):
        status = self._check_length(login)
        if status is True:
            return status
        return status

    def check_with_regular_exp(self, login):
        status = self._check_length(login)
        if status is True:
            start = time.time()
            pattern = ('[a-zA-Z]' if len(login) == 1
                       else '[a-zA-Z]+[0-9a-zA-Z]' if len(login) == 2
                       else '[a-zA-Z]+[0-9a-zA-Z.-]+[0-9a-zA-Z]')
            if re.fullmatch(pattern, login):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status


if __name__ == "__main__":
    login_from_user = input('Введите логин: ')
    login = LoginCheck()
    print(login.check_with_built_in(login_from_user))
    print(login.check_with_prepared_sets(login_from_user))
    print(login.check_with_regular_exp(login_from_user))
