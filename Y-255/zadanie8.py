def cmn(a,b,c):
    if a==b==c:
        return 3
    elif a==b or a==c or b==c:
        return 2
    else:
        return 0
a=int(input())
b=int(input())
c=int(input())
result=cmn(a,b,c)
print(f"Количество совпавших чисел:{result}")