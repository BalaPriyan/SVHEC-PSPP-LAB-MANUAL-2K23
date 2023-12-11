n=int(input("Enter A Number Of Rows:"))
m=(2*n)-2
for i in range(0,n):
    for j in range(0,m):
        print(end="")
    m=m-1
    for i in range(0,i+1):
        print("king",end="")
    print("")
