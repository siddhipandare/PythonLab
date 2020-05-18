

def gcd (big,small):
    
    if (big%small==0):
        return (small)
    else:
        return gcd(small,big%small)

x=int(input("enter value 1:"))
y=int(input('enter value 2:'))
small= min(x,y)
big=max(x,y)
print("GCD is",gcd(big,small))



