#1
x = int(input("Введите число x: "))
print('Все квадраты натуральных чисел, не превосходящие x')
y = 1
while y * y <= x:
    print(y * y)
    y += 1
#2
x = int(input("Введите число x: "))
d = 2
while d <= x and x % d != 0:
    d += 1
print('Наименьший натуральный делитель числа x, отличный от 1')
print(d)
#3
x = int(input("Введите число x: "))
y = 2
s = 1
while y * 2 <= x:
    y *= 2
    s += 1
print("Наибольшая целая степень двойки, не превосходящая N\n" +
      "Показатель степени", s, "\n"  "Значение степени", y)
#4
def z4(x, y):
    d = 1
    while y > x:
        x *= 1.1
        d += 1
    return d
x = int(input("В первый день спортсмен пробежал километров: "))
y = int(input("Минимальное количество километров: "))
print("Номер дня, на который пробег спортсмена составит не менее", y, "километров: ", z4(x, y))
#5
k = 0
while True:
    y = int(input("Введите целое неотрицательное число: "))
    if y >= 0:
        if y == 0:
            break
        else:
            k += 1

print("Количество членов последовательности:", k)
#6
k = 0
summ = 0
while True:
    y = float(input("Введите число: "))
    if y == 0:
        break
    else:
        k += 1
        summ += y

print("Среднее значение всех элементов последовательности:", summ / k)
#7
k = 0
pred = 0
while True:
    y = int(input("Введите натуральное число: "))
    if y >= 0:
        pred = y
        if y == 0:
            break
        elif y > pred:
            k += 1

print("Элементов этой последовательности больше предыдущего элемента", k)

#8
count = 1
max_count = 0
previous_number = 0

while True:
    number = int(input("Введите натуральное число: "))
    if number == 0:
        break
    if previous_number == 0:
        previous_number = number
    elif number == previous_number:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1
        previous_number = number
print("Наибольшее количество подряд идущих одинаковых элементов:", max_count)