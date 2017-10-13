import random
import os

print("***Rules***\n 1] You have 21 sticks , you can take between 1-4 number of sticks, then computer will do same")
print("\n 2] whoever is going to take last stick will be looose game.\n")

sticks = 21
# ch = 'Y'
b = 1
if b == 1:
# while ch!='n'


    while True:

        print("\nsticks available:", sticks)
        if sticks == 0:
            print("\nMatch Draw---Sticks are not available")
            break
          #  ch == (input("!!\t Do you want to play again--> y/n :- "))

        if sticks < 0:
            print("\nLet's play again, computer has broken rules ---Sticks are not available")
            break
          #  ch == (input("!!\t Do you want to play again--> y/n :- "))

        sticks_chosed = int(input("\nEnter number of sticks: "))

        if sticks == 1:
            print("\n(:::  You lost :::)")
            break

        elif sticks_chosed >= 5 or sticks_chosed <= 0:
            print("\nInvalid input,  please read the rules!!!")
            continue

        sticks -= sticks_chosed
        if sticks == 1:
            print("\nyou won")
            break
        else:

            a = int(random.randint(1, 4))
            

            if a <= sticks:
                print("\ncomputer took: ", a)
                sticks -= a
            else:
                sticks -= a
                if sticks < 0:
                    print("\ncomputer broke rules...You won!!!")
                    break
