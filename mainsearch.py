from data import *


def search():
    while True:
        print("===============================")
        print("              SEARCH           ")
        print("===============================")
        print("")
        print("1.  Search Directory By Keyword")
        print("2.  Search Among Categories")
        print("3.  Show WHOLE Databse of Foods")
        print("4.  Return")
        print("")
        print("===============================")
        print("")
        opt = input("Enter Choice : ")
        print("\n")
        if opt != "":  # because blank input is not allowed by int
            intopt = int(opt)
            if intopt == 1:
                searchkey()
            elif intopt == 2:
                categ()
            elif intopt == 3:
                datashow()
            elif intopt == 4:
                break
            else:
                print("Please Enter a VALID Option !!")
        elif opt == "":
            print("An option is required")
            print("\n")
        else:
            print(" PLease Enter a VALID Option !!")
            print("\n")


def categ():
    print("\n")
    print("================================")
    print("            CATEGORIES          ")
    print("================================")
    print("")
    print("1. Breakfast")
    print("2. Snacks")
    print("3. Lunch")
    print("4. Dinner")
    print("================================")
    x = int(input("Enter desired meal: "))
    if x == 1:
        d = Breakfast()
        for item in sorted(d):
            print("------------------------------------------------------------------------------------------")
            print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
            print("------------------------------------------------------------------------------------------")
            break
        for item in sorted(d):
            print(":", item[0], " " * (25 - len(item[0])),
                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                  ":         ", item[2], " " * (8 - len(str(item[2]))),
                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
        print("------------------------------------------------------------------------------------------")
        print("\n")
    elif x == 2:
        d = snacks()
        for item in sorted(d):
            print("------------------------------------------------------------------------------------------")
            print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
            print("------------------------------------------------------------------------------------------")
            break
        for item in sorted(d):
            print(":", item[0], " " * (25 - len(item[0])),
                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                  ":         ", item[2], " " * (8 - len(str(item[2]))),
                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
        print("------------------------------------------------------------------------------------------")
        print("\n")
    elif x == 3:
        d = Lunch()
        for item in sorted(d):
            print("------------------------------------------------------------------------------------------")
            print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
            print("------------------------------------------------------------------------------------------")
            break
        for item in sorted(d):
            print(":", item[0], " " * (25 - len(item[0])),
                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                  ":         ", item[2], " " * (8 - len(str(item[2]))),
                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
        print("------------------------------------------------------------------------------------------")
        print("\n")
    elif x == 4:
        d = dinner()
        for item in sorted(d):
            print("------------------------------------------------------------------------------------------")
            print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
            print("------------------------------------------------------------------------------------------")
            break
        for item in sorted(d):
            print(":", item[0], " " * (25 - len(item[0])),
                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                  ":         ", item[2], " " * (8 - len(str(item[2]))),
                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
        print("------------------------------------------------------------------------------------------")
        print("\n")


def datashow():
    d = datalist()
    print("\n")
    print("=============================")
    print("            FILTERS          ")
    print("=============================")
    filt = input("Want to add Filters (y/n)?:  ")
    print("\n")

    if filt == "y":
        print("1. Protiens")
        print("2. Fats")
        print("")
        print("Feel free to chose multiple options by using '&' between options")
        print("")
        inpfil = input("Enter Choice: ")
        testfil = ""
        profil = 0
        fatfil = 0
        if "&" in inpfil:
            for i in inpfil:
                if i in ["1", "2", "3", "&"]:
                    testfil += i
            lfil = testfil.split("&")  # all options
            for i in lfil:
                if i == "1":
                    profil = 1  # pro
                if i == "2":
                    fatfil = 1  # fat

        if profil == 1 and fatfil == 1:
            for item in sorted(d):
                print("------------------------------------------------------------------------------------------")
                print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
                print("------------------------------------------------------------------------------------------")
                break
            for item in sorted(d):
                print(":", item[0], " " * (25 - len(item[0])),
                      ":         ", item[1], " " * (9 - len(str(item[1]))),
                      ":         ", item[2], " " * (8 - len(str(item[2]))),
                      ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
            print("------------------------------------------------------------------------------------------")
            print("\n")

        elif profil == 1 and fatfil == 0 or inpfil == "1":
            for item in sorted(d):
                print("-------------------------------------------------------------------------")
                print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :")
                print("-------------------------------------------------------------------------")
                break
            for item in sorted(d):
                print(":", item[0], " " * (25 - len(item[0])),
                      ":         ", item[1], " " * (9 - len(str(item[1]))),
                      ":         ", item[2], " " * (8 - len(str(item[2]))), ":"
                      )
            print("-------------------------------------------------------------------------")
            print("\n")

        elif profil == 0 and fatfil == 1 or inpfil == "2":
            for item in sorted(d):
                print("---------------------------------------------------------------------")
                print(":          FOOD ITEM         :       CALORIES      :       FAT      :")
                print("---------------------------------------------------------------------")
                break
            for item in sorted(d):
                print(":", item[0], " " * (25 - len(item[0])),
                      ":         ", item[1], " " * (9 - len(str(item[1]))),
                      ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
            print("---------------------------------------------------------------------")
            print("\n")

    else:
        for item in sorted(d):
            print("----------------------------------------------------")
            print(":          FOOD ITEM         :       CALORIES      :")
            print("----------------------------------------------------")
            break

        for item in sorted(d):
            print(":", item[0], " " * (25 - len(item[0])),
                  ":         ", item[1], " " * (9 - len(str(item[1]))), ":")
        print("----------------------------------------------------")
        print("\n")


def searchkey():
    print("=============================")
    print("            KEYWORD          ")
    print("=============================")
    inp = input("Enter the desired food :  ")
    print("=============================")
    lowinp = inp.lower()
    d = datalist()
    for item in d:
        if lowinp in item[0]:
            print("\n")
            print("=============================")
            print("            FILTERS          ")
            print("=============================")
            filt = input("Want to add Filters (y/n)?:  ")

            print("\n")

            if filt == "y":
                print("1. Protiens")
                print("2. Fats")
                print("")
                print("Feel free to chose multiple options by using '&' between options")
                print("")
                inpfil = input("Enter Choice: ")
                print("=============================")
                testfil = ""
                profil = 0
                fatfil = 0
                if "&" in inpfil:
                    for i in inpfil:
                        if i in ["1", "2", "3", "&"]:
                            testfil += i
                    lfil = testfil.split("&")  # all options
                    for i in lfil:
                        if i == "1":
                            profil = 1  # pro
                        if i == "2":
                            fatfil = 1  # fat

                if profil == 1 and fatfil == 1:
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print(
                                "------------------------------------------------------------------------------------------")
                            print(
                                ":          FOOD ITEM         :       CALORIES      :       PROTIEN      :       FAT      :")
                            print(
                                "------------------------------------------------------------------------------------------")
                            break
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print(":", item[0], " " * (25 - len(item[0])),
                                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                                  ":         ", item[2], " " * (8 - len(str(item[2]))),
                                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
                    print("------------------------------------------------------------------------------------------")
                    print("\n")
                    break
                elif profil == 1 and fatfil == 0 or inpfil == "1":
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print("-------------------------------------------------------------------------")
                            print(":          FOOD ITEM         :       CALORIES      :       PROTIEN      :")
                            print("-------------------------------------------------------------------------")
                            break
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print(":", item[0], " " * (25 - len(item[0])),
                                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                                  ":         ", item[2], " " * (8 - len(str(item[2]))), ":"
                                  )
                    print("-------------------------------------------------------------------------")
                    print("\n")
                    break
                elif profil == 0 and fatfil == 1 or inpfil == "2":
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print("---------------------------------------------------------------------")
                            print(":          FOOD ITEM         :       CALORIES      :       FAT      :")
                            print("---------------------------------------------------------------------")
                            break
                    for item in sorted(d):
                        if lowinp in item[0]:
                            print(":", item[0], " " * (25 - len(item[0])),
                                  ":         ", item[1], " " * (9 - len(str(item[1]))),
                                  ":      ", item[3], " " * (7 - len(str(item[3]))), ":")
                    print("---------------------------------------------------------------------")
                    print("\n")
                    break
            else:
                for item in sorted(d):
                    if lowinp in item[0]:
                        print("----------------------------------------------------")
                        print(":          FOOD ITEM         :       CALORIES      :")
                        print("----------------------------------------------------")
                        break

                for item in sorted(d):
                    if lowinp in item[0]:
                        print(":", item[0], " " * (25 - len(item[0])),
                              ":         ", item[1], " " * (9 - len(str(item[1]))), ":")
                print("----------------------------------------------------")
                print("\n")
                break

    else:
        print("No Such RESULTS FOUND in DATABASE")
