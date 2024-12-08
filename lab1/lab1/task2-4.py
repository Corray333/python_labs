#3,8,16
import random

def shuffle_string(string):
    words = string.split()
    random.shuffle(words)
    return ' '.join(words)

def count_even_words(string):
    count = 0
    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            count += 1
    return count

def russian_flag(mas):
    white = mas.index('Белый')
    blue = mas.index('Синий')
    red = mas.index('Красный')

    new_mas = [mas[white], mas[blue], mas[red]]
    return new_mas


def choose_task():
    print("Выберите задачу:")
    print("1. Перемешать слова в строке")
    print("2. Подсчитать количество слов с четным количеством букв")
    print("3. Функция 'Флаг России'")

    choice = input("Введите номер задачи (1, 2, или 3): ")

    if choice == '1':
        string = input("Введите строку для перемешивания: ")
        print("Результат:", shuffle_string(string))
    elif choice == '2':
        string = input("Введите строку для подсчета слов с четным количеством букв: ")
        print("Количество слов с четным количеством букв:", count_even_words(string))
    elif choice == '3':
        mas = ['Синий', 'Белый', 'Красный']
        print("Результат:", russian_flag(mas))
    else:
        print("Неверный выбор, попробуйте снова.")
        choose_task()

# Запуск выбора задачи
choose_task()