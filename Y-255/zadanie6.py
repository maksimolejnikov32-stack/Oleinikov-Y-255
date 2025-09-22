def sc(x1,y1,x2,y2):
    return "Да" if (x1+y1)%2==(x2+y2)%2 else "Нет"
    
data= list(map(int,input("Введите 4 числа (x1 y1 x2 y2):").split()))
if len(data)==4 and all(1<=num<=8 for num in data):
    result=sc(data[0],data[1],data[2],data[3])
    print (result)
else:
    print("Ошибка")