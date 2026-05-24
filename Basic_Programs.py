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
'''Write a program to print the following pattern :

      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 

'''
'''
a=int(input("Enter the number of Rows :"))
b=1
c=1
print("The pattern is : \n")
for i in range(a,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for l in range(0,b):
        print("*",end=" ")
    for k in range(0,b-1):
        print("*",end=" ")
    print("",end="\n")
    b=b+1
for i in range(a-1,0,-1):
    for j in range(0,c):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(0,i-1):
        print("*",end=" ")
    print("",end="\n")
    c=c+1
    
'''
###############################################################################################################################
'''Write the code to print the following pattern :

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

'''
'''
a=int(input("Enter the number of rows :"))
for i in range(0,a):
    if i==0 or i==a-1:
        for j in range(0,a):
            print("*",end=" ")
        print("",end="\n")
    else:
        for j in range(0,a):
            if j==0 or j==a-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("",end="\n")
            
'''
###############################################################################################################################
'''Write a program to print the following pattern

        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 

'''
'''
a=int(input("Enter the number of rows :"))
b=1
c=1
for i in range(a,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(0,b):
        if k==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for l in range(b-1,0,-1):
        if l==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    b=b+1
    print("",end="\n")
for i in range(a-1,0,-1):
    for j in range(0,c):
        print(" ",end=" ")
    for k in range(0,i):
        if k==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for l in range(i-1,0,-1):
        if l==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    c=c+1
    print("",end="\n")

'''
#################################################################Strings##########################################################

#Write a program program to print the user entered name followed by "Good afternoon"
'''
a=input("Enter your name : ")
b=a+" Good afternoon"
print(b)
'''
#################################################################################################################################

'''Create a string made of the first, middle, and last character
Practice Problem: Write a program to create a new string made of an input strings first, middle, and last characters.

Exercise Purpose: This exercise teaches the fundamentals of String Indexing. Accessing specific positions, especially
the middle that requires calculating length, is a foundational skill for data parsing and text manipulation.

Given Input: str1 = "James"

Expected Output: Jms
'''
'''
a=input("Enter the string :")
b=len(a)
c=a[0]
d=a[b//2]
e=a[b-1]
c=c+d+e
print("The output string : ",c)

'''
##############################################################################################################################
'''Practice Problem: Write a program to create a new string made of the middle three characters of an input string of odd length.

Exercise Purpose: This builds on indexing by introducing String Slicing. Slicing is a powerful Python feature
that lets you extract entire “chunks” of data efficiently.

Given Input: str1 = "JhonDipPeta"

Expected Output: Dip
'''
'''
a=input("Enter the string :")
b=len(a)
c=a[b//2-1]+a[b//2]+a[b//2+1]
print("The middle three characters of the string are : ",c)
'''
##############################################################################################################################
'''Practice Problem: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.

Exercise Purpose: This exercise introduces String Partitioning and Concatenation. In programming, you often need to “inject” data
into a template or modify strings at specific locations.

Given Input: s1 = "Ault" s2 = "Kelly"

Expected Output: AuKellylt
'''
'''
a=input("Enter the string 1 :")
b=input("Enter the string 2 :")
c=len(a)//2
d=a[:c]+b+a[c:]
print("The new string is : ",d)
'''
##############################################################################################################################
'''Practice Problem: Write a program to reverse a given string.

Exercise Purpose: Reversing a string is a classic logic-building exercise. In Python, this is most efficiently done via 
Slicing, demonstrating the languages ability to manipulate sequences using “steps.” It is a prerequisite for solving problems 
like palindrome detection.

Given Input: str1 = "PYnative"

Expected Output: evitanYP
'''
a=input("Enter the string : ")
c=a[-1::-1]
print("The reverse string is :",c)
###############################################################################################################################
