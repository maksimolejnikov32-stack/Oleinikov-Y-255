# 1.1
x=int(input("Введите количество элементов массива: "))
a=[]
for i in range(x):
    element=int(input(f"Введите элемент {i + 1}: "))
    a.append(element)
max_element=max(a)
print("Максимальный элемент:", max_element)
print("Массив в обратном порядке:", a[::-1])
# 1.2
import numpy as np
a=list(map(float, input("Введите массив действительных чисел: ").split()))
mean_value=np.mean(a)
a=[mean_value if x == 0 else x for x in a]
print("Измененный массив:", a)
# 2.1
N=int(input("Введите количество элементов массива: "))
a=[]

for i in range(x):
    element = int(input(f"Введите элемент {i + 1}: "))
    a.append(element)
min_element=min(a)
min_index=a.index(min_element)
print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)
#2.2
N=int(input("Введите количество элементов массива: "))
a=[]
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    a.append(element)
min_element = min(a)
min_index = a.index(min_element)
print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)
#3.1
D=list(map(int, input("Введите массив D через пробел: ").split()))
sum=sum(D[i] for i in range(1, len(D), 2))
print("Массив D:", D)
print("Сумма элементов с нечетными индексами:", sum)
#3.2
a=list(map(int, input("Введите массив из 8 элементов через пробел: ").split()))
for i in range(len(a)):
    if a[i]<15:
        a[i]*=2
print("Преобразованный массив:", a)
#4.1
a=list(map(int, input("Введите массив целых чисел: ").split()))
maxelem=max(a)
maxind=a.index(max_element)
print("max element крч:", maxelem)
print("Порядковый номер max:", maxind + 1)
#4.2
a=list(map(int, input("Введите массив целых чисел: ").split()))
odd=[x for x in a if x % 2 != 0]
if odd:
    odd.sort(reverse=True)
    print("Нечетные числа в порядке убывания:", odd)
else:
    print("Нечетных чисел нет.")
#5.1
a=list(map(int, input("Введите массив из 10 целых чисел: ").split()))
for i in range(len(a)-1):
    if a[i]<0 and a[i + 1]<0:
        print(f"Пара отрицательных чисел: {a[i]}, {a[i+1]}")
#5.2
a = list(map(int, input("Введите массив из 10 целых чисел: ").split()))
ua = list(set(a))
print("Массив без одинаковых элементов:", ua)
#6.1
a=list(map(int, input("Введите массив из 10 целых чисел: ").split()))
m=sum(a)/len(a)
less=sum(1 for x in a if x<m)
greater=sum(1 for x in a if x>m)
print(f"Количество элементов меньше среднего: {less}")
print(f"Количество элементов больше среднего: {greater}")
#6.2
a=list(map(int, input("Введите массив из 10 целых чисел: ").split()))
greater=sum(x for x in a if x > 5)
print("Сумма чисел больше 5:", greater)
#7.1
a=list(map(int, input("Введите массив целых чисел: ").split()))
suma=sum(a[i] for i in range(0, len(a), 2))
product=1
for i in range(1, len(a), 2):
    product*=a[i]
print("Сумма элементов с четными индексами:", suma)
print("Произведение элементов с нечетными индексами:", product)
#7.2
a = list(map(int, input("Введите массив целых чисел: ").split()))
min_index=a.index(min(a))
max_index=a.index(max(a))
a[min_index], a[max_index] = a[max_index], a[min_index]
print("Массив после перестановки минимального и максимального элементов:", a)













