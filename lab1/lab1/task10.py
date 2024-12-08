#10 - Дан список строк с клавиатуры. Упорядочить по количеству слов в строке
def read_and_sort_by_word_count():
    # Считываем количество строк
    n = int(input("Введите количество строк: "))
    
    # Чтение списка строк
    strings = []
    for i in range(n):
        string = input(f"Введите строку {i+1}: ")
        strings.append(string)
    
    # Сортировка списка по количеству слов в строке
    sorted_strings = sorted(strings, key=lambda str: len(str.split()))
    
    # Вывод отсортированного списка
    print("\nСтроки, отсортированные по количеству слов:")
    for string in sorted_strings:
        print(string)

# Запуск функции
read_and_sort_by_word_count()
