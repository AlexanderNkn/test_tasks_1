import re
import time


class LoginCheck:
    """Проверяет соответствие вводимого логина заданным параметрам.

    Для проверки были использованы 3 метода:
    - с помощью build-in методов
    - сравнением с подготовленными сетами
    - с помощью регулярных выражений
    """
    def _check_length(self, login):
        if not login:
            return 'Вы не ввели логин'
        if len(login) > 20:
            return 'Вы ввели слишком длинный логин'
        return True

    def _split_login(self, login):
        """Делит логин на 3 части, так как разная логика проверки."""
        first = login[0]
        middle = login[1:-1]
        last = login[-1] if len(login) > 1 else []
        return first, middle, last

    def check_with_built_in(self, login):
        """Проверяет логин с помощью build-in методов python."""
        status = self._check_length(login)
        if status is True:
            start = time.time()
            first, middle, last = self._split_login(login)
            if (
                first.isalpha()
                and (not middle
                     or middle.isalpha()
                     or middle.isdecimal()
                     or {'.'}.issubset(middle)
                     or {'-'}.issubset(middle))
                and (not last or last.isalpha() or last.isdecimal())
            ):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status

    def check_with_prepared_sets(self, login):
        """Проверяет логин сравнивая с подготовленными выборками."""
        status = self._check_length(login)
        if status is True:
            start = time.time()
            first, middle, last = self._split_login(login)
            set_for_first = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')  # noqa
            set_for_middle = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890.-')  # noqa
            set_for_last = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')  # noqa
            if (
                set(first).issubset(set_for_first)
                and set(middle).issubset(set_for_middle)
                and set(last).issubset(set_for_last)
            ):
                end = time.time()
                return f'Логин корректный. Время проверки {end-start}'
            end = time.time()
            return f'Логин НЕ корректный. Время проверки {end-start}'
        return status

    def check_with_regular_exp(self, login):
        """Проверяет логин с помощью регулярных выражений."""
        status = self._check_length(login)
        if status is True:
            start = time.time()
            pattern = (
                '[a-zA-Z]'
                if len(login) == 1
                else '[a-zA-Z]+[0-9a-zA-Z]'
                if len(login) == 2
                else '[a-zA-Z]+[0-9a-zA-Z.-]+[0-9a-zA-Z]'
            )
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
