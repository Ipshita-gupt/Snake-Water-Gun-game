import random

''' 
 1 for snake
 -1 for water
 0 for gun
'''

computer = random.choice([1,-1,0])
youstr = input("enter your choice: ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1: "snake", -1 : "water", 0 : "gun"}

you = youdict[youstr]
print(f"you chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("this match is draw")

else:
    if(computer == 1 and you == 0):
        print("you win")
    elif(computer == 1 and you == -1):
        print("you lose")
    elif(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you lose")
    else:
        print("something went wrong")




