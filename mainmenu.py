from mainsearch import *
from datacalculator import *
from mainpersonaldetails import *
from foodplaner import *


def Loggedinmenu(name, height, weight, age, gender):
    n = name
    h = height
    w = weight
    a = age
    g = gender
    while True:
        print("=====================================")
        print("                 MENU                ")
        print("=====================================")
        print("")
        print("1.    SEARCH")
        print("2.    FOOD PLANNER")
        print("3.    PERSONAL DETAILS")
        print("4.    FOOD CART")
        print("5.    EXIT")
        print("")
        print("=====================================")
        x = (input("Enter desired choice: "))
        print("\n")
        if x in ["1", "2", "3", "4", "5"]:
            if int(x) == 1:
                search()
            elif int(x) == 2:
                foodplan(h, w, a, g)
            elif int(x) == 3:
                personaldetailmenu(n, h, w, a, g)
            elif int(x) == 4:
                datacalc()
            elif int(x) == 5:
                break


def guestmenu():
    while True:
        print("=====================================")
        print("                 MENU                ")
        print("=====================================")
        print("")
        print("1.    SEARCH")
        print("2.    FOOD CART")
        print("3.    RETURN")
        print("")
        print("=====================================")
        x = (input("Enter desired choice: "))
        print("\n")
        if x in ["1", "2", "3"]:
            if int(x) == 1:
                search()
            elif int(x) == 2:
                datacalc()
            elif int(x) == 3:
                break
