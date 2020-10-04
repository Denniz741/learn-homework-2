"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv
def main():

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    user_dict = [
             {'name' : 'Alex', 'age': '38', 'job': 'adjuster'},
             {'name': 'Den', 'age' : '45', 'job': 'software developer'},
             {'name': 'Andre', 'age': '35', 'job' : 'electronics engineer'},
             {'name': 'Nicole', 'age': '33' , 'job': 'sales Manager'}
          ]

    with open('users.csv','w',encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_dict:
            writer.writerow(user)

if __name__ == "__main__":
    main()

