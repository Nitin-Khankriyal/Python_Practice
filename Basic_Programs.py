#Program to print "Hello world"
'''
print("Hello world")
'''
###############################################################################################################################
#Program to print the output of the arithmetic operators
'''
a=int(input("Enter the first Number : "))
b=int(input("Enter the second Number : "))
c=a+b;
d=a-b;
e=a*b;
f=a/b;
print("The addition of the number is ",c)
print("The subtraction of the number is ",d)
print("The multiplication of the number is ",e)
print("The division of the number is ",f)
'''
################################################################################################################################
#Program to convert Decimal number to number system
'''
a=int(input("Enter the  decimal number :"))
sum=0
i=0
while a>0:
    n=a%10
    sum=n*pow(2,i)+sum
    i=i+1
    a=a//10
print("The number is ",sum)
'''
##################################################################################################################################
#Write a program whether a number is the Palimdrome number of not
'''
a=int(input("Enter the Number :"))
n=a
sum=0
while n>0:
    b=n%10
    sum=sum*10+b
    n=n//10
if a==sum:
    print("The number is the Palindrome Number")
else:
    print("The number is not the Palindrome number")
'''
#################################################################################################################################
#Write a program to check whether a number is the Armstrong Number or not
'''
a=int(input("Enter the number :"))
n=a
sum=0
digit=0
while n>0:
    n=n//10
    digit=digit+1
n=a
while n>0:
    b=n%10
    sum=pow(b,digit)+sum
    n=n//10
if a==sum:
    print("The number is the armstrong Number")
else:
    print("The number is not the armstrong number")
'''
#################################################################################################################################

'''Write a program to print the following pattern :

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''

'''
a=int(input("Enter the number of Rows :"))
b=1
print("The pattern is : \n")
for i in range(a,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(0,b):
        print("*",end=" ")
    for k in range(0,b-1):
        print("*",end=" ")
    print("",end="\n")
    b=b+1
'''
#################################################################################################################################

'''Write a program to print the following pattern :

* 
* * 
* * * 
* * * * 
* * * * * 

'''
'''
a=int(input("Enter the number of Rows :"))
print("The pattern is : \n")
for i in range(1,a+1):
    for j in range(0,i):
        print("*",end=" ")
    print("",end="\n")

'''
#############################################################################################################################

'''Write the program to print the following pattern :

* * * * * 
* * * * 
* * * 
* * 
* 

'''
'''
a=int(input("Enter the number of Rows :"))

print("The pattern is : \n")
for i in range(a,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("",end="\n")

'''
################################################################################################################################

'''Write the program to print the following pattern

* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

'''
'''
a=int(input("Enter the number of Rows :"))
b=0
print("The pattern is : \n")
for i in range(a,0,-1):
    for j in range(0,b):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    for k in range(0,i-1):
        print("*",end=" ")
    print("",end="\n")
    b=b+1

'''
#################################################################################################################################