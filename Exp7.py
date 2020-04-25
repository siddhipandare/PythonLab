''' PROBLEM STATEMENT: 
Given a non-negative integer A, print all the pairs of integers(a,b) such that
a and b are positive integers
a<=b and
a^2 + b^2 = A
0 <= A
A<=1000
'''

A=int(input(""))
for i in range (0,A+1):
    for j in range (i,A+1):
        if i**2 + j**2 == A:
            print("({},{})".format(i,j),end=" ")
    
    