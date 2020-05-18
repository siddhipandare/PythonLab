def func(x,y,z):
    #t=(4*x+y+2*z-4)
    #t=20*x+y-2*z-17
    t=(4-5*x-3*y-7*z)
    t=round(t,3)
    return t

def funcx(y,z):
    #x=0.25*(4-y-2*z)
    #x=(1/20)*(17-y+2*z)
    x=(1/5)*(4-3*y-7*z)
    return x
def funcy(x,z):
    #y=0.2*(7-z-3*x)
    #y=(1/20)*(-18-3*x+z)
    y=(1/26)*(9-3*x-2*z)
    return y
def funcz(x,y):
    #z=(1/3)*(3-x-y)
    #z=(1/20)*(25-2*x+3*y)
    z=(1/11)*(5-7*x-2*y)
    return z

def seidel(x,y,z,count):
    x1= funcx(y,z)
    y1= funcy(x1,z)
    z1= funcz(x1,y1)
    r= func(x1,y1,z1)
    if(abs(r)<0.0000000000000000001):
        print("The root of the equation is at:({},{},{})".format(round(x1,5),round(y1,5),round(z1,5)))
        print("the number of iterations are: ",count)
    else:
        seidel(x1,y1,z1,count+1)


seidel(0,0,0,0)