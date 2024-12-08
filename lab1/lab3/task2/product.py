import random

N = 10

with open("numbers.txt", "w") as file1:
    numbers = [random.randint(1, 100) for _ in range(N)]
    file1.write(" ".join(map(str, numbers)))

with open("products.txt", "w") as file2:
    product = 1
    products = []
    for number in numbers:
        product *= number
        products.append(product)
    file2.write(" ".join(map(str, products)))
