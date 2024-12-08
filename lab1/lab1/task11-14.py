#Задания 3,5,9,11
# Отсортировать строки:
#3 - В порядке увеличения разницы между частотой наиболее часто встречаемого символа в строке и частатой его появления в алфавите
#5 - В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого в строке символа от частоты его встречаемости в текстах на этом алфавите
#9 - В порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально расположенным символов строки (относительно ее середины)
#11 - В порядке квадратичного отклоения диспресии максимального среднего веса ASCII-кода тройки символов в первой строке


import re
from collections import Counter

alphabet_frequency = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

def diff_most_frequent_to_alphabet_frequency(s):
    # Подсчитываем частоты символов
    counts = Counter(s.lower())
    most_frequent_char, most_frequent_count = counts.most_common(1)[0]
    
    # Вычисляем частоту появления символа в строке
    most_frequent_char_frequency = most_frequent_count / len(s)
    
    # Извлекаем частоту символа из алфавита
    alphabet_freq = alphabet_frequency.get(most_frequent_char, 0)
    
    # Разница частот
    return abs(most_frequent_char_frequency - alphabet_freq)

def variance_of_frequency(s):
    counts = Counter(s.lower())
    most_frequent_char, most_frequent_count = counts.most_common(1)[0]
    
    most_frequent_char_frequency = most_frequent_count / len(s)
    alphabet_freq = alphabet_frequency.get(most_frequent_char, 0)
    
    # Квадратичное отклонение
    return (most_frequent_char_frequency - alphabet_freq) ** 2
    

def variance_of_ascii_pairs(s):
    s = s.strip()
    max_ascii = max(map(ord, s))
    
    n = len(s)
    differences = []
    
    for i in range(n // 2):
        left = ord(s[i])
        right = ord(s[n - i - 1])
        differences.append(abs(left - right))
    
    if differences:
        avg_difference = sum(differences) / len(differences)
    else:
        avg_difference = 0
    
    return (max_ascii - avg_difference) ** 2
    
    
def max_ascii_triplet_variance(s):
    n = len(s)
    if n < 3:
        return float('inf')
    
    triplet_averages = []
    
    for i in range(n - 2):
        triplet = s[i:i+3]
        avg = sum(map(ord, triplet)) / 3
        triplet_averages.append(avg)
    
    if triplet_averages:
        max_avg = max(triplet_averages)
        variance = sum((x - max_avg) ** 2 for x in triplet_averages) / len(triplet_averages)
    else:
        variance = 0
    
    return variance
    
# Задача #3
def task_3(strings):
    return sorted(strings, key=diff_most_frequent_to_alphabet_frequency)

# Задача #5
def task_5(strings):
    return sorted(strings, key=variance_of_frequency)
    

# Задача #9
def task_9(strings):
    return sorted(strings, key=variance_of_ascii_pairs)

# Задача #11
def task_11(strings):    
    return sorted(strings, key=max_ascii_triplet_variance)

# Пример использования
strings = [
    "hello", "jj9f8938h8hb", "test", "some random text", "a b c d e f g h"
]

# Выбор задачи
def choose_task():
    print("Выберите задачу:")
    print("1. Упорядочить по увеличению разницы частоты самого частого символа и частоты его в алфавите (Задача #3)")
    print("2. Упорядочить по увеличению квадратичного отклонения частоты самого частого символа (Задача #5)")
    print("3. Упорядочить по увеличению квадратичного отклонения ASCII-кодов зеркальных символов (Задача #9)")
    print("4. Упорядочить по квадратичному отклонению дисперсии ASCII-кодов троек (Задача #11)")

    choice = input("Введите номер задачи (1, 2, 3, или 4): ")

    if choice == '1':
        result = task_3(strings)
    elif choice == '2':
        result = task_5(strings)
    elif choice == '3':
        result = task_9(strings)
    elif choice == '4':
        result = task_11(strings)
    else:
        print("Неверный выбор, попробуйте снова.")
        return

    print("\nРезультат сортировки:")
    for string in result:
        print(string)

# Запуск
choose_task()
