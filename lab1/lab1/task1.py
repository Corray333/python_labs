def gcd(num, begin_of_range):
    while begin_of_range != 0:
        num, begin_of_range = begin_of_range, num % begin_of_range
    return num

def digits(num):
    return [int(d) for d in str(num)[::-1]]

# Количество взаимнопростых чисел
def count_of_deviders(num):
    count = 0
    for i in range(1, num):
        if gcd(num, i) == 1:
            count += 1
    return count

# Сумма цифр, делящихся на 3
def sum_of_digits(num):
    return sum(i for i in digits(num) if i % 3 == 0)

# Найти делитель, являющийся взаимно простым с цифрами числа
def specific_devider(num):
    num = abs(num)
    for i in range(2, num):
        if num % i == 0:
            count = sum(gcd(i, j) == 1 for j in digits(num))
            if count == len(digits(num)):
                return i
    return -1

# Получение чисел от пользователя
num1 = int(input("Введите число для подсчета взаимно простых чисел: "))
num2 = int(input("Введите число для суммы цифр, делящихся на 3: "))
num3 = int(input("Введите число для поиска специального делителя: "))

# Вывод результатов
print(f"Количество взаимно простых чисел: {count_of_deviders(num1)}")
print(f"Сумма цифр числа, делящихся на 3: {sum_of_digits(num2)}")
print(f"Делитель: {specific_devider(num3)}")