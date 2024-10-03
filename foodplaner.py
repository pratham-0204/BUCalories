from data import *
from random import *
from All_in_one_Cal import *


def foodplan(h, w, a, g):
    print(
        "-----------------------------------------------------------------------------------------------------------------------------")
    print(
        "                                                        Food Planner                                                         ")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------")
    print("")
    height = h
    weight = w
    age = a
    gender = g

    def calorie(height=height, weight=weight):
        current_cal = Calories_calculate(height, weight, age, gender)
        gm = 1
        B = round(weight // (height ** 2), 2)
        if B < 22:
            w = weight
            h = height
            while True:
                new_weight = w + gm / 1000
                t = (new_weight) / h ** 2
                gm += 10
                if t > 22 and t < 23:
                    break
            total = (gm / 1000) * 7000
            current_data = f'''
_____________________________________________________________________________________
Your Current Bmi is                                       :  {B}
_____________________________________________________________________________________
Extra weight required to be in fit category               :  {round(gm / 1000, 1)} 
_____________________________________________________________________________________
Calories you should take a day (600 Calories than usual)  :  {int(current_cal + 600)}    
_____________________________________________________________________________________
No. of days to be in fit range                            :  {total // 600}
_____________________________________________________________________________________

            '''

            return int(current_cal + 600), current_data
        elif B > 23:
            h = height
            w = weight
            while True:
                new_weight = w - gm / 1000
                t = (new_weight) / h ** 2
                gm += 10
                if t > 22 and t < 23:
                    break
            total = (gm / 1000) * 7000
            current_data = f'''
_____________________________________________________________________________________
Your Current Bmi is                                            : {B}
_____________________________________________________________________________________
weight required to be deducted to be in fit category           :  {round(gm / 1000, 1)} 
_____________________________________________________________________________________
Calories you should take a day (500 less Calories than usual)  :  {int(current_cal - 500)}  
_____________________________________________________________________________________
No. of days to get into fit range                              :  {total // 500}
_____________________________________________________________________________________

'''
            return int(current_cal - 500), current_data
        else:
            current_data = f'''
_____________________________________________________________________________________
Your Current Bmi is                                       : {B}
_____________________________________________________________________________________
You are in fit category
_____________________________________________________________________________________
Calories you should take a day                            :  {int(current_cal)}    
_____________________________________________________________________________________

'''

            return int(current_cal), current_data

    def fullmeal():
        b = 0.275 * calorie()[0]
        l = 0.375 * calorie()[0]
        s = 0.075 * calorie()[0]
        d = 0.275 * calorie()[0]
        return b, l, s, d

    def roti(c=calorie()[0]):
        if c < 1500:
            return 250
        elif c <= 2000 and c > 1500:
            return 350
        elif c > 2000 and c <= 2500:
            return 400
        elif c > 2500 and c <= 300:
            return 450
        elif c > 3000:
            return 500

    def rotirice(c=calorie()[0]):
        if c < 1500:
            return 120, 120
        elif c <= 2000 and c > 1500:
            return 170, 100
        elif c > 2000 and c <= 2500:
            return 200, 120
        elif c > 2500 and c <= 300:
            return 220, 120
        elif c > 3000:
            return 270, 120

    def rice(c=calorie()[0]):
        if c < 1500:
            return 120
        elif c <= 2000 and c > 1500:
            return 250
        elif c > 2000 and c <= 2500:
            return 300
        elif c > 2500 and c <= 3000:
            return 350
        elif c > 3000:
            return 450

    def breakfastt():
        b = Breakfast()
        newb = [x for x in b if x not in breakfast_less()]
        shuffle(newb)
        newbcal = newb[0][0]
        # print(newbcal)
        bless = breakfast_less()
        shuffle(bless)
        return (
            f"For breakfast    : {int((100 / data()[newbcal][0]) * fullmeal()[0]) - 10} gms {newb[0][0]} , {bless[0][0]} and {bless[1][0]}")

    def lunchh(p):
        if p == "1":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = lunch_less()
            shuffle(bless)
            r = "roti"
            if abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - int((1 / 3) * (roti())))) < 30:
                t = randint(30, 40)
            elif abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - int((1 / 3) * (roti())))) > 600:
                t = randint(500, 600)
            else:
                t = abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - int((1 / 3) * (roti()))))
            return (
                f"For lunch        : {t} gms {newb[0][0]} , {int((1 / 3) * roti())} gms roti  , {bless[0][0]} and {bless[1][0]}")
        elif p == "2":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = lunch_less()
            shuffle(bless)
            r = "roti"
            if abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - (1 / 3 * (rotirice()[0])))) - 100 < 30:
                t = randint(30, 40)
            else:
                t = abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - (1 / 3 * (rotirice()[0])))) - 100
            return (
                f"For lunch        : {t} gms {newb[0][0]} , {int(1 / 3 * roti())} gms roti, {100} gms rice  , {bless[0][0]} and {bless[1][0]}")
        elif p == "3":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = lunch_less()
            shuffle(bless)
            return (
                f"For lunch        : {abs(int(((100 / data()[newbcal][0]) * fullmeal()[1]) - 10 - (10 / 13 * rice())))} gms {newb[0][0]} , {int(10 / 13 * rice())} gms rice  , {bless[0][0]} and {bless[1][0]}")

    def snackss():
        b = snacks()
        newb = [x for x in b if x not in snacks_less()]
        shuffle(newb)
        newbcal = newb[0][0]
        bless = snacks_less()
        shuffle(bless)
        return (
            f"For snacks       : {int((100 / data()[newbcal][0]) * fullmeal()[2]) - 10} gms {newb[0][0]} , {bless[0][0]} and {bless[1][0]}")

    def dinnerr(p):
        if p == "1":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = dinner_less()
            shuffle(bless)
            r = "roti"
            return (
                f"For dinner       : {abs(int(((100 / data()[newbcal][0]) * fullmeal()[3]) - 10 - (1 / 4 * (roti()))))} gms {newb[0][0]} , {int(1 / 4 * roti())} gms roti , {bless[0][0]} and {bless[1][0]}")
        elif p == "2":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = dinner_less()
            shuffle(bless)
            r = "roti"
            if abs(int(((100 / data()[newbcal][0]) * fullmeal()[3]) - 10 - (1 / 4 * (rotirice()[0])))) - 100 < 30:
                t = randint(30, 40)
            else:
                t = abs(int(((100 / data()[newbcal][0]) * fullmeal()[3]) - 10 - (1 / 4 * (rotirice()[0])))) - 100
            return (
                f"For dinner       : {t} gms {newb[0][0]} , {int(1 / 4 * roti())} gms roti, {100} gms rice , {bless[0][0]} and {bless[1][0]}")
        elif p == "3":
            b = dishes()
            newb = b
            shuffle(newb)
            newbcal = newb[0][0]
            bless = dinner_less()
            shuffle(bless)
            return (
                f"For dinner       : {abs(int(((100 / data()[newbcal][0]) * fullmeal()[3]) - 10 - (10 / 13 * rice())))} gms {newb[0][0]} , {int(10 / 13 * rice())} gms rice , {bless[0][0]} and {bless[1][0]}")

    while True:
        print("Enter your preference : ")
        print("1.Only roti ")
        print("2.Rice with roti")
        print("3.Only rice")
        p = input("Enter your choice: ")
        if p == "1":
            print(
                "______________________________________________________________________________________________________________________________")
            print(breakfastt())
            print(
                "______________________________________________________________________________________________________________________________")
            print(lunchh('1'))
            print(
                "______________________________________________________________________________________________________________________________")
            print(snackss())
            print(
                "______________________________________________________________________________________________________________________________")
            print(dinnerr("1"))
            print(
                "______________________________________________________________________________________________________________________________")
            print("")
            print(calorie()[1])
            print("")
            break
        elif p == "2":
            print(
                "______________________________________________________________________________________________________________________________")
            print(breakfastt())
            print(
                "______________________________________________________________________________________________________________________________")
            print(lunchh('2'))
            print(
                "______________________________________________________________________________________________________________________________")
            print(snackss())
            print(
                "______________________________________________________________________________________________________________________________")
            print(dinnerr("2"))
            print(
                "______________________________________________________________________________________________________________________________")
            print("")
            print(calorie()[1])
            print("")
            break
        elif p == "3":
            print(
                "______________________________________________________________________________________________________________________________")
            print(breakfastt())
            print(
                "______________________________________________________________________________________________________________________________")
            print(lunchh('3'))
            print(
                "______________________________________________________________________________________________________________________________")
            print(snackss())
            print(
                "______________________________________________________________________________________________________________________________")
            print(dinnerr("3"))
            print(
                "______________________________________________________________________________________________________________________________")
            print("")
            print(calorie()[1])
            print("")
            break
        else:
            print("Please enter a correct input.")
            print("")
