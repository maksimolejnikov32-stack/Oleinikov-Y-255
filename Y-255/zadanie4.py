def fn(a,b,l,N):
    return(l*2)+(2*(b*(N-1)))+(2*(a*N)-a)
a=int(input("Расстояние между рядами: "))
b=int(input("Расстояние между дырочками: "))
l=int(input("Дырочек в ряду: "))
N=int(input("Длина свободного шнурка: "))
print(fn(a,b,l,N))