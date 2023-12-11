def circulate (a,n):
    for i in range(1,n+1):
        b=a[i:]+a[:i]
        print("circulation",i,"=",b)
a=[91,92,93,94,95,96,97,98]
n=int(input("enter n :"))
circulate(a,n)
