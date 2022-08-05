from fireDetection import fire
from recorder import video
from preydetect import det
def menu():
    print("[1] : video recording ")
    print("[2] : Moment detection ")
    print("[3] : fire alarm system ")

menu()
option=int(input("enter the integer value to use the specific feature : "))

while option!=0:
    if option==1:
        video()
    elif option==2:
        det()

    elif option==3:
        fire()
    else:
        print("you\'ve entered an invalid option")
    print()
    menu()
    option=int(input("enter the integer value to use the specific feature"))
