
#Pattern 1
for i in range(1,7):
    for j in range(1,i):
        print("*",end="")
    print(end="\n")
print() 
print() 
#Pattern 2
n=4 #int(input("enter the row"))
for i in range (1,n+1):
    print(' '*(n-i)+"*"*i)
print() 
print() 
#Pattern 3
n= 4 #int(input("enter the row"))
m=40
for i in range (1,n+1):
    print(' '*(40-i)+"* "*i)  
print() 
print() 
#Pattern 4
n= 4  #int(input("enter the row"))
for i in range (0,n):
    print(" "*i+"*"*(n-i)) 
print() 
print() 

#Tables
for i in range(1,11):
    for j in range(1,11):
        print("{:2}".format(i*j), end="  ")
    print(end="\n") 
print() 
print() 
#Pattern 5
s="python" #input("enter the word")
n=len(s)
for i in range(1,n+2):
    for j in range(1,i):
        print(s[j-1],end="")
    print(end="\n")

for i in range(0,n+2):
    print(s[0:i])

print() 
print() 
#Pattern 6
n=4 #int(input("enter the value: "))
for i in range (1,n+1):
    for j in range (1,n+1):
        print("{:2}".format(max(i,j,(n+1)-i,(n+1)-j)),end="")
    print() 

k=1
for i in range (1,6):
    for j in range (1,3):
        print("{}".format(k))
        k=k+1

print() 
print() 
#Pattern 7
n=4   #int(input("enter the value: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("* "*(n-i),end="")
    print("* "*(n-(i+1)),end=" ")
    print(end='\n') 

print() 
print() 
#Pattern 8
n=  4 #int(input("enter the value: "))
for i in range (1,n+1):
    for j in range (1,n+1):
        print("{:2}".format(max(i,j,(n+1)-i,(n+1)-j)),end="")
    print() 
print() 