'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity 
if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered 
or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the 
integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, 
and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
'''
'''
class Solution(object):
    def myAtoi(self, s):

        temp = 0
        count = 0
        sign = 1
        for i in s:
            if i == " " and count == 0 and temp == 0:
                continue
            elif (i == "-" or i == "+") and count == 0 and temp == 0:
                if i == "-":
                    sign = -1
                count = 1
            elif i.isdigit():
                a = int(i)
                temp = temp * 10 + a
                count = 1
            else:
                break
        temp = temp * sign
        if temp < -2**31:
            return -2**31
        if temp > 2**31 - 1:
            return 2**31 - 1
        return temp
'''
#################################################################################################################################
'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to 
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a=[]
        temp=0
        j=0
        p=""
        for i in range(0,numRows):
            a.append("")
        for i in s:
            a[j]=a[j]+i
            if temp==0:
                j=j+1
            if temp==1:
                j=j-1
            if j==numRows-1:
                temp=1
            if j==0:
                temp=0
        for i in a:
            p=p+i
        return p
obj=Solution()
print(obj.convert("PAYPALISHIRING",3))
'''
##################################################################################################################################
#Given a roman numeral, convert it to an integer.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=len(s)
        result=0
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(0,a):
            if i==a-1:
                result=result+d[s[i]]
            elif d[s[i]]>=d[s[i+1]]:
                result=result+d[s[i]]
            else:
                result=result-d[s[i]]  
        return result            
obj=Solution()
print(obj.romanToInt("MCMXCIV"))
'''
#############################################################################################################################
#Given an integer, convert it to a Roman numeral.
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        a=num
        str=""
        times=0
        while num!=0:
            for i in d:
                if i<=num:
                    p=i
                    break
            times=num//p
            str=str+(d[p]*times)
            num=num-(p*times)
        return str
obj=Solution()
print(obj.intToRoman(1994))
'''