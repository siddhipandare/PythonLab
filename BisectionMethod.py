import math as m
def f(x):
    return ((x*x)-2*x-8)

def bi(a,b,c):
    t= float((a+b)/2)

    if (abs(f(t))<0.0001):
        print("The root of the equation is: ",m.ceil(t))
        print("no. of iterations: ",c)
        return t

        

    else:
        if f(t)>0:
            b=t
            
            bi(a,b,c+1)
            
        elif f(t)<0:
            a=t
            
            bi(a,b,c+1)

x=int(input("enter the value of a: "))
y=int(input("enter the value of b: "))
 

bi(x,y,0)