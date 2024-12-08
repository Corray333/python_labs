#Задания 3,8,16
import re

# Задача #3: Найти количество русских символов
def count_russian_letters(string):
    russian_letters = re.findall(r'[А-Яа-я]', string)
    return len(russian_letters)

# Задача #8: Найти количество латинских символов
def count_latin_letters(string):
    latin_letters = re.findall(r'[A-Za-z]', string)
    return len(latin_letters)

# Задача #16: Найти минимальное целое число
def find_min_integer(string):
    numbers = re.findall(r'-?\d+', string)  # Находим все числа, включая отрицательные
    if numbers:
        min_number = min(map(int, numbers))  # Преобразуем строки в числа и ищем минимум
        return min_number
    else:
        return "Нет целых чисел"

# Функция для выбора задачи
def choose_task():
    print("Выберите задачу:")
    print("1. Найти количество русских символов в строке")
    print("2. Найти количество латинских символов в строке")
    print("3. Найти минимальное из имеющихся в строке целых чисел")

    choice = input("Введите номер задачи (1, 2, или 3): ")

    if choice == '1':
        string = input("Введите строку: ")
        print("Количество русских символов:", count_russian_letters(string))
    elif choice == '2':
        string = input("Введите строку: ")
        print("Количество латинских символов:", count_latin_letters(string))
    elif choice == '3':
        string = input("Введите строку: ")
        print("Минимальное целое число:", find_min_integer(string))
    else:
        print("Неверный выбор, попробуйте снова.")
        choose_task()

# Запуск выбора задачи
choose_task()
