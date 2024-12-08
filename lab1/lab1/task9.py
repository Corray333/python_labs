def read_and_sort_strings():
    # Считываем количество строк
    n = int(input("Введите количество строк: "))
    
    # Чтение списка строк
    strings = []
    for i in range(n):
        string = input(f"Введите строку {i+1}: ")
        strings.append(string)
    
    # Сортировка списка по длине строки
    sorted_strings = sorted(strings, key=len)
    
    # Вывод отсортированного списка
    print("\nСтроки, отсортированные по длине:")
    for string in sorted_strings:
        print(string)

# Запуск функции
read_and_sort_strings()
