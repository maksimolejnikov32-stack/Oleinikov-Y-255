#1
x = 1
y = 10
for z in range(x, y + 1):
    print(z)

#2
x = 10
y = 1
if x < y:
    for z in range(x, y + 1):
        print(z)
else:
    for z in range(x, y - 1, -1):
        print(z)

#3
x = 10
y = 1
for z in range(x, y - 1, -1):
    if z % 5 != 0:
        print(z)

#4
x = 0
for _ in range(1, int(input('Введите число N ')) + 1):
    x += int(input('Введите число '))
print('Сумма ', x)

#5
x = 0
for z in range(1, int(input('Введите натуральное число ')) + 1):
    x += z ** 3
print(x)

#6
x = 1
for z in range(1, int(input('Факториал числа ')) + 1):
    x *= z
print(x)

#7
x = int(input("Введите число n: "))
total_sum = 0
current_fact = 1
for z in range(1, x + 1):
    current_fact *= z
    total_sum += current_fact
print("Сумма факториалов от 1 до", x, ":", total_sum)

#8
x = int(input("Введите число n (До 9, натуральное ):"))
if x > 9 or x < 0:
    print('Число n не подходит под условия')
for z in range(1, x + 1):
    print(''.join(map(str, range(1, z + 1))))

#9
x = int(input("Введите число n (количество чисел из ряда Фибоначчи):"))
y, y = 0, 1
sum_fibonacci = y
for _ in range(x - 1):
    sum_fibonacci += y
    y, y = y, y + y

print("Сумма первых", x, "чисел ряда Фибоначчи:", sum_fibonacci)

#10
M = int(input("Введите количество чисел из ряда Фибоначчи: "))
K = int(input("Введите стартовый индекс: "))

x, y = 0, 1
for _ in range(K - 1):
    x, y = y, x + y

sum_fibonacci = 0
for _ in range(M):
    sum_fibonacci += x
    x, y = y, x + y

print("Сумма", M, "чисел ряда Фибоначчи, начиная с", K, ":", sum_fibonacci)