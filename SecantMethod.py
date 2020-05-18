
from math import *
def f(x):
    return(x*exp(x)-cos((x)))

""" def f(x):
    return(3*x-sin(x)-exp(x)) """

"""  def f(x):
    return(x**4-x-10) """
    
""" def f(x):
    return(x*sin(x)-0.5)  """




def err(a,b):
    e= abs((b-a)/a)
    return e

def secant(x0,x1,count):
    x2= x1 -((f(x1)*(x1-x0))/(f(x1)-f(x0)))

    if(err(x1,x2)<0.0000001):
        print("the root is: ",x2)
        print("error of convergence is:",err(x1,x2))
        print("no. of iterations: ",count)
    else:
        x0=x1
        x1=x2
        count=count+1
        secant(x0,x1,count)


m,n=[int(x) for x in input ("enter range: ").split() ]

secant(m,n,0)


    

