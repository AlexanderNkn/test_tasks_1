import os
import sys
from unittest import mock

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def login_check():
    from login import LoginCheck
    return LoginCheck()


def test_login_lenght(login_check):
    answer = login_check._check_length
    assert answer('') == 'Вы не ввели логин'
    assert answer('123456789012345678901') == 'Вы ввели слишком длинный логин'
    assert answer('aaaaa') is True


@mock.patch('time.time', mock.MagicMock(return_value=12345))
def test_check_with_built_in(login_check):
    answer = login_check.check_with_built_in
    assert answer('a') == 'Логин корректный. Время проверки 0'
    assert answer('a1') == 'Логин корректный. Время проверки 0'
    assert (answer('1a') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Первый символ - латинская буква'
    assert answer('a1a') == 'Логин корректный. Время проверки 0'
    assert answer('a1.-a') == 'Логин корректный. Время проверки 0'
    assert (answer('a1.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Последний символ - латинская буква или цифра'
    assert (answer('a1@.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'из не букв и не цифр допускаются точка и минус'
    assert answer('Aa1.-a.A') == 'Логин корректный. Время проверки 0'


@mock.patch('time.time', mock.MagicMock(return_value=12345))
def test_check_with_prepared_sets(login_check):
    answer = login_check.check_with_prepared_sets
    assert answer('a') == 'Логин корректный. Время проверки 0'
    assert answer('a1') == 'Логин корректный. Время проверки 0'
    assert (answer('1a') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Первый символ - латинская буква'
    assert answer('a1a') == 'Логин корректный. Время проверки 0'
    assert answer('a1.-a') == 'Логин корректный. Время проверки 0'
    assert (answer('a1.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Последний символ - латинская буква или цифра'
    assert (answer('a1@.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'из не букв и не цифр допускаются точка и минус'
    assert answer('Aa1.-a.A') == 'Логин корректный. Время проверки 0'


@mock.patch('time.time', mock.MagicMock(return_value=12345))
def test_check_with_regular_exp(login_check):
    answer = login_check.check_with_regular_exp
    assert answer('a') == 'Логин корректный. Время проверки 0'
    assert answer('a1') == 'Логин корректный. Время проверки 0'
    assert (answer('1a') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Первый символ - латинская буква'
    assert answer('a1a') == 'Логин корректный. Время проверки 0'
    assert answer('a1.-a') == 'Логин корректный. Время проверки 0'
    assert (answer('a1.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'Последний символ - латинская буква или цифра'
    assert (answer('a1@.-a.') == 'Логин НЕ корректный. Время проверки 0'
            ), 'из не букв и не цифр допускаются точка и минус'
    assert answer('Aa1.-a.A') == 'Логин корректный. Время проверки 0'
