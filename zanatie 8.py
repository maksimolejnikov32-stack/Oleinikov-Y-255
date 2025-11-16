#1.1
import math
def square_rectangle(length, width):
    return length * width
def square_circle(radius):
    return math.pi * radius ** 2
def square_triangle(base, height):
    return 0.5 * base * height
#Пример
print("Площадь прямоугольника:", square_rectangle(5, 10))
print("Площадь круга:", square_circle(7))
print("Площадь треугольника:", square_triangle(5, 12))
#1.2
def sum_and_average(array):
    total = sum(array)
    average = total / len(array)
    return total, average
array1 = [1, 2, 3]
array2 = [4, 5, 6]
array3 = [7, 8, 9]
for i, array in enumerate([array1, array2, array3], start=1):
    total, average = sum_and_average(array)
    print(f"Массив {i}: Сумма = {total}, Среднее арифметическое = {average}")
#2.1
def area_triangle(a):
    return(math.sqrt(3)/4)*a**2
def area_hexagon(a):
    return(3 * math.sqrt(3)/2)*(a**2)
# Пример использования
sl=5
print("Площадь правильного шестиугольника:", area_hexagon(sl))
#2.2
def area_rectangle(l, w):
    return l * w
rectangles = [(3,4),(5,6),(7,8)]
for i,(l, w) in enumerate(rectangles,start=1):
    print(f"Площадь прямоугольника {i}:{area_rectangle(l,w)}")
#3.1
import math
def hypo(a, b):
    return math.sqrt(a**2+b**2)
t1 = (3, 4)
t2 = (6, 8)
h1 = hypo(*t1)
h2 = hypo(*t2)
if h1 > h2:
    print("Гипотенуза первого больше.")
else:
    print("Гипотенуза второго больше.")
#3.2
def sort_words(sentence):
    words = sentence.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)
input_string = "hello world"
print("Отсортированная строка:", sort_words(input_string))
#4.1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def divide_fractions(A,B,C,D):
    numerator=A*D
    denominator=B*C
    common_divisor=gcd(numerator,denominator)
    return numerator//common_divisor,denominator//common_divisor
A,B,C,D = 1,2,3,4
result=divide_fractions(A,B,C,D)
print(f"Результат:{result[0]}/{result[1]}")
#4.2
def is_inside_circle(x_a,y_b,r,point):
    x_p,y_p=point
    return (x_p-x_a)**2+(y_p-y_b)**2<r**2
points=[(1,1),(5,5),(0,0)]
circle_center=(0,0)
radius=5
inside_count=sum(is_inside_circle(circle_center[0], circle_center[1], radius, p) for p in points)
print(f"Количество точек внутри окружности: {inside_count}")
#5.1
def subtract_fractions(A,B,C,D):
    numerator=A*D-B*C
    denominator=B*D
    common_divisor=gcd(numerator,denominator)
    return numerator//common_divisor,denominator//common_divisor
A,B,C,D=5,6,3,4
result_subtract=subtract_fractions(A,B,C,D)
print(f"Результат вычитания дробей: {result_subtract[0]}/{result_subtract[1]}")
#5.2
def divisors(n):
    return [i for i in range(1,n+1) if n%i==0]
number=int(input("Введите число: "))
print("Делители числа:",' '.join(map(str,divisors(number))))
#6.1
def d(a,b):
    while b:
        a,b=b,a%b
    return a
def c(a,b):
    return abs(a*b)//d(a,b)
A=12
B=15
print("НОД:",d(A, B))
print("НОК:",c(A, B))
#6.2
def S(a,b,c,d,diagonal):
    s1=(a+b+diagonal)/2
    a1=math.sqrt(s1*(s1-a)*(s1-b)*(s1-diagonal))
    s2=(c+d+diagonal)/2
    a2=math.sqrt(s2*(s2-c)*(s2-d)*(s2-diagonal))
    return a1+a2
a=5
b=6
c=7
d=8
diagonal=4
print("Площадь:",S(a,b,c,d,diagonal))
#7.1
def a_rectangle(length,width):
    return length*width
def a_triangle(base,height):
    return (base*height)/2
X=4
Y=3
a_quad=a_rectangle(X,Y)+a_triangle(X,Y)
print("Площадь четырехугольника:",a_quad)
#7.2
def to_octal(n):
    return format(n, '010o')
number = int(input("Введите неотрицательное целое число: "))
print("Восьмеричный код:", to_octal(number))








