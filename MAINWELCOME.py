from LOGINSIGNUP import *

from mainmenu import *


def main():
    while True:
        print("=====================================")
        print("             BU Calories             ")
        print("=====================================")
        print("")
        print("1. Login")
        print("2. Register")
        print("3. Continue as a Guest")
        print("4. EXIT")
        print("")
        print("=====================================")
        x = int(input("Enter Desired Choice : "))
        print("\n")

        if x == 1:
            login()
            break
        elif x == 2:
            register()
        elif x == 3:
            guestmenu()
        elif x == 4:
            break
        else:
            print("Enter A Valid Choice")
            print("\n")


main()
