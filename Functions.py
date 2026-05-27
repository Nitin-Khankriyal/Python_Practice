#Write a function to reverse the string
'''
def reverse_string(a):
    b=a[-1::-1]
    return b
a=input("Enter the String : ")
print("The reverse of the string is : ",reverse_string(a))
'''
############################################################################################################################
#Write a function to print fibonacci series
'''
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    a=fibonacci(n-1)+fibonacci(n-2)
    return a
a=int(input("Enter the limit :"))
print("The Series is :")
for i in range(1,a+1):
    print(fibonacci(i),end="\t")
'''
###########################################################################################################################
#Write the program to convert the decimal number to binary number
'''
def dectobinary(a):
    if a==0:
        return 0
    temp=dectobinary(a//2)*10+a%2
    return temp
a=int(input("Enter the Decimal Number : "))
print("The binary number is : ",dectobinary(a))
'''
###########################################################################################################################
#Write the program to convert the binary number to decimal number
'''
def binarytodec(a):
    i=0
    temp=0
    while a!=0:
        b=a%10
        temp=temp+b*pow(2,i)
        i=i+1
        a=a//10
    return temp
a=int(input("Enter the binary Number : "))
print("The binary number is : ",binarytodec(a))
'''
###########################################################################################################################
#Write the check whether a number is the palindrome number or not
'''
def palindrome(a):
    n=a
    temp=0
    while n!=0:
        b=n%10
        temp=temp*10+b
        n=n//10
    if temp==a:
        return 1
    else:
        return 0
a=int(input("Enter the number : "))
if palindrome(a)==1:
    print("The numeber is the Palindrome Number")
else:
    print("The numeber is not the Palindrome Number")
'''
###########################################################################################################################
#Write the program to print the factorial of the number using recursion
'''
def factorial(a):
    if a==1:
        return 1
    temp=factorial(a-1)*a
    return temp
a=int(input("Enter the number : "))
print("The factorial of the number is : ",factorial(a))
'''
###########################################################################################################################
#Write the program to calculate the power of the number
'''
def power(a,n):
    if n==1:
        return a
    temp=power(a,n-1)*a
    return temp
a=int(input("Enter the number : "))
n=int(input("Enter the Power of the number : "))
print("The factorial of the number is : ",power(a,n))
'''
###########################################################################################################################
#Write the program to generate all the subsequences of the string
'''
def subsequences(a):
    s=[]
    def backtrack(index,b):
        if index==len(a):
            s.append(b)
            return
        backtrack(index+1,b+a[index])
        backtrack(index+1,b)
    backtrack(0,"")
    return s
a=input("Enter the String : ")
print(subsequences(a))
'''
###########################################################################################################################
#Write the program to find the subsets of the set which sum equal to number n given by user 
'''
def sum_of_subsets(a,n,s):
    if n==0:
        print(s)
        return
    if len(a)==0 and n!=0:
        return
    if n<0:
        return
    b=a.pop()
    sum_of_subsets(a.copy(),n,s.copy())
    s.add(b)
    sum_of_subsets(a.copy(),n-b,s.copy())
    
s={20,10,15,35,30}
print("The subsets are : ")
sum_of_subsets(s,50,set())
'''