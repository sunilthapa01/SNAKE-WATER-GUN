import random
import time 

print("\n\n\n\n")

print("\t\t\t--------------------------------------------------------------------------------")
print("\t\t\t||                                                                            ||")
print("\t\t\t||______________________________Snake , Water and Gun_________________________||")
print("\t\t\t||                                                                            ||")
print("\t\t\t||                                                                            ||")
print("\t\t\t--------------------------------------------------------------------------------")
print("\n\n")
time.sleep(3)
Nam = input("\t\t Enter your Name :: ")
Nam_upper = Nam.upper()

print("\n")
print("\t\t\t\tProcessing...........")

time.sleep(5)
print("\t\t\t---------------------------------------------------------")
print("\t\t\t||                                                     ||")
print(f"\t\t\t||   WELCOME {Nam_upper} OUR GAME SNAKE,WATER AND GUN !!!!   ||")
print("\t\t\t||                                                     ||")
print("\t\t\t---------------------------------------------------------")

print("\n\n\n")
# Snake Water Gun 
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("COMP TURN: \t\t1. Snake(s) \n\t\t\t2. Water(w)\n\t\t\t3.  Gun(g) ")
print("\n\n\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
print("\n\n")
print("\t\t\t\tProcessing.............................")
time.sleep(3)

print("\n\n")
you = input("YOUR TURN: \t\t1. Snake(s) \n\t\t\t2. Water(w)\n\t\t\t3. Gun(g)\n\t\t Choose :::")
a = gameWin(comp, you)
print("\n")
print("\t\t\t **************************************")
print("\t\t\t ||                                  ||")
print("\t\t\t ||   COMPUTER CHOOSE {}             ||".format(comp))
print("\t\t\t ||                                  ||")
print("\t\t\t **************************************")
print("\n")
print("\t\t\t **************************************")
print("\t\t\t ||                                  ||")
print("\t\t\t ||   YOU CHOOSE {}                  ||".format(you))
print("\t\t\t ||                                  ||")
print("\t\t\t **************************************")
time.sleep(3)
print("\n\n")
print("\t\t\t||                  ||")
print("\t\t\t||     YOUR RESULT  ||")
print("\t\t\t||                  ||")

print("\n\n\n")
if a == None:

    print("\t\t\t-----------------------------")
    print("\t\t\t||                         ||")
    print("\t\t\t||    The game is a tie!   ||")
    print("\t\t\t||                         ||")
    print("\t\t\t-----------------------------")

elif a:
    print("\t\t\t-----------------------------")
    print("\t\t\t||                         ||")
    print("\t\t\t||        You Win !!!!     ||")
    print("\t\t\t||                         ||")
    print("\t\t\t-----------------------------")
else:
    print("\t\t\t----------------------------")
    print("\t\t\t||                        ||")
    print("\t\t\t||       You Lose !!!!    ||")
    print("\t\t\t||                        ||")
    print("\t\t\t----------------------------")



print("\n\n\n\n")

print("\t\t\t||----------------------------------THANK YOU------------------------------------||")

print("\n\n\n")