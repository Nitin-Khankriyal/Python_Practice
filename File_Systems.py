'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.'''
'''
a=open("poems.txt","r")
b=a.read()
c="twinkle"
if c in b:
    print("It contains the word twinkle......")
else:
    print("It does not contain the word twinkle.....")
a.close()
'''
#########################################################################################################################
'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever 
the game() function breaks the Hi-score.'''
'''
import random
def game():
    a=random.randint(0,101)
    return a
a=open("High-score.txt","r+")
b=game()
p=a.read()
if p.isdigit():
    c=eval(p)
else:
    c=0
print(b)
if b>c:
    a.write(str(b))
a.close()
'''
#############################################################################################################################
'''A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. '''
'''
a=open("donkey.txt","r")
b=a.read()
a.close()
p=open("donkey.txt","w")
c=b.replace("donkey","#####")
p.write(c)
print(c)
p.close()
'''
############################################################################################################################
#Write a program to find out the line number where the word 'python' is present in the file
'''
a=open("poems.txt","r")
c=True
line=0
while(c):
    c=a.readline()
    line=line+1
    if "python" in c:
        print("Line",line,"contains the word 'python'")
        break
a.close()
'''
###########################################################################################################################
'''Write a program to find out whether a file is identical & matches the content of
another file.'''
'''
a=open("poems.txt","r")
b=open("donkey.txt","r")
c=a.read()
d=b.read()
if c==d:
    print("The file are identical")
else:
    print("The file are not identical")
a.close()
b.close()
'''
##########################################################################################################################
#Write a python program to rename a file "poems.txt" to “renamed_by_ python.txt".
'''
import os
os.rename("poems.txt","renamed_by_python.txt")
'''
##########################################################################################################################\