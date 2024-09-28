import random
'''
rock = 1
paper = -1
scissor = 0
'''

computer = random.choice([1,-1,0])
yourstr = input("Enter your choice: ")
yourDict = { "r":1, "p":-1, "s":0}
you = yourDict[yourstr]
reverseDict = {1:"Rock", -1:"Paper", 0:"Scissor"}

print (f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if (computer == you):
    print ("It's a draw.")
else:
    if (computer == 1 and you == -1):
            r = "Win"
    elif (computer == -1 and you == 0):
            r = "Win"
    elif (computer == 0 and you == 1):
            r = "Win"
    elif (computer == 1 and you == 0):
            r = "Lose"
    elif (computer == 0 and you == -1):
            r = "Lose"
    elif (computer == -1 and you == 1):
            r = "Lose"
    else:
            print("Something went wrong!")
        
    print (f"You {r}")      
 
