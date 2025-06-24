import random

'''
1 for Snake
-1 for Water
0 for Gun

'''

Computer = random.choice([bqa-1,0,1])
youStr = input("Enter Your Choice:- ")
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[Computer]}")

if(Computer == you):
    print("It's a Draw...Try Again")
    
else:
    if(Computer == -1 and you == 1):
        print("You Wins!")
    elif(Computer == -1 and you == 0):
        print("Computer Wins!")
    elif(Computer == 1 and you == -1):
        print('Computer Wins!')
    elif(Computer == 1 and you == 0):
        print('You Wins!')
    elif(Computer == 0 and you == -1):
        print('You Wins!')
    elif(Computer == 0 and you == 1):
        print('Computer Wins!')
        
    else:
        print("Something went wrong...!")
    