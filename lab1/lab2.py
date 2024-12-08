# # Task 1
# n = int(input("Write n = "))
# for i in range (2,n+1):
#     if (n%i == 0):
#         print (i)
#         break
    
# # Task 2
# n = int(input("Write n = "))
# step = 0
# while (n%2 == 0):
#     step += 1
#     n /= 2
# print(step)

# # Task 3
# n = int(input("Write n = "))
# a = int(input())
# index = 0
# index_max = 0
# while (a != 0):
#     index += 1
#     if a > n:
#         n = a
#         index_max = index
#     a = int(input())
# print("Индекс: ", index_max)

# Task 4
# n = int(input("Введите n = "))
# list = []
# while (n != 0):
#     list.append(n)
#     n = int(input("Введите n = "))
# count = 1
# now = 1
# for i in range(len(list)-1):
#     if (list[i] == list[i+1]):
#         now += 1
#         count = max(count, now)
#     else:
#         now = 1
# print("Количество: ", count)

# # Task 5
# first_max = int(input("Первый элемент = "))
# second_max = int(input("Второй элемент = "))
# if first_max < second_max:
#     first_max, second_max = second_max, first_max
# element = int(input())
# while element != 0:
#     if element > first_max:
#         second_max, first_max = first_max, element
#     elif element > second_max:
#         second_max = element
#     element = int(input("Write element = "))
# print(second_max)

# # Task 6
n = int(input("Введите число = "))
factorial = 1
sum = 0
for i in range(1, n + 1):
    factorial *= i
    sum += factorial