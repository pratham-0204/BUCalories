from All_in_one_Cal import *
import csv
from mainsearch import *
from mainmenu import *


def register():
    print("=====================================")
    print("              REGISTER               ")
    print("=====================================")
    with open('user2.csv', mode='a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        name = input("Name : ")
        height = get_height()
        weight = get_weight()
        age = get_age()
        gender = sex()
        passw = input("Password : ")
        passw2 = input("Confirm Password : ")
        if passw == passw2:
            writer.writerow([name, passw, height, weight, age, gender])
            print('\n    SUCCESSFULLY REGISTERED!!')
            print("=====================================")
        else:
            print('\n     [PASSWORDS DO NOT MATCH !!]')
            print("=====================================")


def login():
    print("=====================================")
    print("                LOGIN                ")
    print("=====================================")
    name = input('Name : ')
    passw = input('Password : ')
    with open('user2.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if [name, passw] == [row[0], row[1]]:
                print('\n         WELCOME BACK !!', name)
                name = row[0]
                height = float(row[2])
                weight = float(row[3])
                age = int(row[4])
                gender = row[5]
                Loggedinmenu(name, height, weight, age, gender)
                return True
        print('\n[PROVIDED CREDENTIALS ARE INVALID!]')
        print("=====================================")
        return False
