## Stone Paper Scissors ##

import random

print("Welcome to game /n Let's play with you")

print("1 for stone /n 2 for Paper /n 3 for scissors")

a = int(input("Enter your choice: "))
b = random.randint(1,3)

print(f"you choose: {a}")
print(f"comp choose: {b}")

while (a!=1 and a!=2 and a!=3):
    print("You entered Invalid input")
    break

if (a==b):
    print("it's Draw try again")
elif (a==1 and b==2 or a==2 and b==3 or a==1 and b==1):
    print("you won")
else:
    print("You loose")


print("Thanks for playing with me :) ")  






## The perfect guess ##

from random import randint as r

a = r(1,100)
b = -1

guess = 0

while(b!=a):
    b = int(input("Guess the no: "))

    if(b<a):
        print("Higher no plzz")
        guess +=1
    else:
        print("Lower no plzz")
        guess +=1
         
print(f"you guess the correct no {a} in {guess} attempt")

