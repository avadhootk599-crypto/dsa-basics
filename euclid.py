def euclid(x,y):
    if x<y:
        (x,y)=(y,x)
    while(x%y !=0):
        diff=x-y
        (x,y)=(max(x,diff),min(x,diff))

    return y

def naive(x,y):
    gcd=0
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
x=int(input("enter the value of first integer :"))
y=int(input("enter the value of second integer :"))
print("by euclid :")
print(euclid(x,y))
print("by naive")
print(naive(x,y))
