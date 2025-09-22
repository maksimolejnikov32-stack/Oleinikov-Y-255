def ch(n,m,k):
    total=n*m
    if k>total or k<=0:
        return "Нет"
    if (k%n==0 and k//n<=m) or (k%m==0 and k//m<=n):
        return "Да"
n=int(input())
m=int(input())
k=int(input())
result=ch(n,m,k)
print(result)