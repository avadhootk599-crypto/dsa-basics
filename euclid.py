def euclid(x,y):
    if x<y:
        (x,y)=(y,x)
    while(x%y !=0):
        diff=x-y
        (x,y)=(max(x,diff),min(x,diff))

    return y

x=int(input("enter the value of first integer :"))
y=int(input("enter the value of second integer :"))
print(euclid(x,y))