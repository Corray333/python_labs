# Задачи 9, 21, 33, 45, 57

#9 - Дан целочисленный массив. Необходимо найти элементы, расположенные перед посленим минимальным
#21 - Дан целочисленный массив. Необходимо найти элементы, расположенные после первого максимального
#33 - Дан целочисленный массив.  Проверить, чередуются ли в нем положительные и отрицательные числа
#45 - Дан целочисленный массив и интервал a..b, необходимо найти сумму элементов, значение которых попадает в этот интервал
#57 - Для введенного списка найти количество таких элементов, которые больше, чем сумма всех предыдущих\

def find_elements_before_last_min(arr):
    #Находит элементы, расположенные перед последним минимальным
    min_element = min(arr)
    last_min_index = len(arr) - 1 - arr[::-1].index(min_element)
    return arr[:last_min_index]

def find_elements_after_first_max(arr):
    #Находит элементы, расположенные после первого максимального
    max_element = max(arr)
    first_max_index = arr.index(max_element)
    return arr[first_max_index + 1:]

def check_alternating_signs(arr):
    #Проверяет, чередуются ли положительные и отрицательные числа
    for i in range(1, len(arr)):
        if arr[i] * arr[i - 1] >= 0:
            return False
    return True

def sum_elements_in_interval(arr, a, b):
    #Находит сумму элементов, значения которых попадают в интервал a..b
    return sum(x for x in arr if a < x < b)

def count_elements_greater_than_previous_sum(arr):
    #Находит количество элементов, которые больше суммы всех предыдущих
    count = 0
    total_sum = 0
    for num in arr:
        if num > total_sum:
            count += 1
        total_sum += num
    return count

def choose_task():
    #Предлагает пользователю выбрать задачу для решения
    print("Выберите задачу для решения:")
    print("1 - Найти элементы, расположенные перед последним минимальным")
    print("2 - Найти элементы, расположенные после первого максимального")
    print("3 - Проверить, чередуются ли положительные и отрицательные числа")
    print("4 - Найти сумму элементов в интервале a..b")
    print("5 - Найти количество элементов, которые больше, чем сумма всех предыдущих")

    choice = int(input("Введите номер задачи: "))

    if choice in [1, 2, 3, 4, 5]:
        arr = list(map(int, input("Введите целочисленный массив через пробел: ").split()))

    if choice == 1:
        print("Элементы перед последним минимальным:", find_elements_before_last_min(arr))
    elif choice == 2:
        print("Элементы после первого максимального:", find_elements_after_first_max(arr))
    elif choice == 3:
        print("Чередуются ли положительные и отрицательные числа:", check_alternating_signs(arr))
    elif choice == 4:
        a, b = map(int, input("Введите интервал a и b через пробел: ").split())
        print("Сумма элементов в интервале:", sum_elements_in_interval(arr, a, b))
    elif choice == 5:
        print("Количество элементов, больше суммы всех предыдущих:", count_elements_greater_than_previous_sum(arr))
    else:
        print("Некорректный выбор!")

# Запуск программы
choose_task()
