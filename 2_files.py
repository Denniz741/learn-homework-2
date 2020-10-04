"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as refer_2:
           ref2 = refer_2.read()
    length = len(ref2)
    len_word = ref2.replace(',', ' ').replace('.',' ').replace('!',' ').replace(':',' ')\
        .replace('"', ' ').replace('-'," ").split()
    quantity_word = len(len_word)
    referat2 = ref2.replace('.','!')
   
    
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(referat2 + '\n  Длина строки равна ' + str(length) + '\n Количество слов равно ' \
             + str(quantity_word))




if __name__ == "__main__":
    main()
