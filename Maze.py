import random

def path2():
    choice3 = input("\nleft or forward? (l/f): ").lower()
    if choice3 == "l":
        path1()
    elif choice3 == "f":
        print("\nYou found your way out. \nYOU WIN")
    else:
        print("´\nInvalid \nGAME OVER")


def path1():
    choice2 = input("\nleft, Right or middle? (l/m/r): ").lower()
    if choice2 == "l":
        rand1 = random.randint(1, 20)
        if rand1 < 5:
            path2()
        elif rand1 >= 5 and rand1 <13:
            path3()
        else:
            path1()
    elif choice2 == "r":
        rand1 = random.randint(1,3)
        if rand1 == 1:
            path3()
        elif rand1 ==2:
            path1()
        else:
            print("\nYou fell into a trap. \nGAME OVER")

    elif choice2 == 'm':
        rand1 = random.randint(1,2)
        if rand1 == 1:
            print("\nWrong turn! \nGAME OVER")

        else:
            path2()
    else:
        print("Invalid \nGAME OVER")


def path3():
    choice4 = input("\nmiddle or right? (m/r): ").lower()
    if choice4 == "m":
        rand1 = random.randint(1,2)
        if rand1 == 1:
            path1()
        else:
            path2()
    elif choice4 == "r":
        rand1 = random.randint(1,2)
        if rand1 == 1:
            path3()
        else:
            print("You ran into a monster. \nGAME OVER")

start = input("Start Game? (Y/N): ").lower()

if start == "y":
    choice1 = input("\nLeft or Right? (l/r): ").lower()

    if choice1 == "l":
        rand1 = random.randint(1,3)

        if rand1 == 1:
            path1()

        elif rand1 == 2:
            path2()

        elif rand1 == 3:
            path3()

        else:
            print("You took the wrong path and got lost. Game Over")






    elif choice1 == "r":
        path2()

    else:
        print("invalid, you lose")



else:
    print("Goodbye")



