def vy(y):
    return (y%4==0 and y%100!=0) or(y%400==0)
y=int(input())
if vy(y):
    print("Високосный год")
else:
    print("Невисокосный год")