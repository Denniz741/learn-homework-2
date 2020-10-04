"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime,timedelta
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    delta = timedelta(days = 1)
    delta1 = timedelta(days = 30)
    dt_now = datetime.now()
    dt_estd = dt_now - delta
    dt_back30 = dt_now - delta1
    print(dt_now)
    print(dt_estd)
    print(dt_back30)

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    date_string = "01/01/20 12:10:03.234567"
    datetime.strptime(date_string,'%m/%d/%y %H:%M:%S.%f')
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
