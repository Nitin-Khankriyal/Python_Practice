import random
d={"rock":-1,"paper":0,"scissors":1}
r={-1:"Rock",0:"Paper",1:"Scissors"}
computer=random.choice([-1,0,1])

a=input("Enter Your Choice from 'rock' , 'Paper' or 'Scissors': ")
b=a.lower()
user_choice=d[b]
print("Your choice : ",a)
print("Compter choice : ",r.get(computer))
if user_choice==computer:
    print("There is a draw")
elif computer==-1 and user_choice==0:
    print("You Wins!!!!")
elif computer==1 and user_choice==-1:
    print("You Wins!!!!")
elif computer==0 and user_choice==1:
    print("You Wins!!!!")
else:
    print("You lose!!!!")