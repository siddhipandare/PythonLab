
 


""" def f(x):
    return ((2*x*x*x)-9.5*x+7.5)
def g(x):
    return ((6*x*x)-9.5) """


def f(x):
    return ((x*x)-24)
def g(x):
    return ((2*x)) 
""" def f(x):
    return ((x*x)-5*x+4)
def g(x):
    return ((2*x)-5) """

def np(m,c):

    x1=m-(f(m)/g(m))
    
    if (abs(x1-m)<0.000000000001):
        print("Root of the equation is: ",x1)
        print("no. of iterations: ",c)
        
    
    else:
        m=x1
        np(m,c+1)

x=int(input("enter the value of x:"))
np(x,0)
