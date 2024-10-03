from data import *
from mainsearch import *
from graphpie import *


def datacalc():
    c = 0
    p = 0
    f = 0
    n = 1
    d = data()
    l = []
    print("")
    print(
        "---------------------------------------------------------------------------------------------------------------------------")
    print(
        "                                                      CALORIE CALCULATOR                                                   ")
    print(
        "---------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("Please enter the items:")
    print("")
    print("INPUT FORMAT --> 'ITEM' WEIGHT (in gm) (default = 100)")
    print("          Eg --> Cucumber 50    (enter d when done)")
    print("")
    while True:
        r = input(f"Enter item no.{n} : ").lower()
        if r.endswith(" "):
            r = r[0:-1]


        def inpu(r):
            if len(r.split()) > 1:
                rs = r.split()
                num = rs[-1]
                if num[0] in [str(x) for x in range(0, 10)]:

                    s = " ".join(str(x) for x in rs[0:-1])
                    x = s
                    return x, rs[-1]
                else:
                    return r, 100
            else:
                return r, 100

        x = inpu(r)
        # print(x)

        # ratio = (int(x[1]))/100
        if x[0] == "d":
            break
        elif x[0] == "" or (x[0] not in d):
            print("")
            print("Sorry the input item is not in our list , please input any other item")
            print("If you want to check the whole menu type (y/n)")
            t = input().lower()
            if t == "y":
                datashow()
                print("INPUT FORMAT --> 'ITEM' WEIGHT (in gm) (default = 100)")
                print("          Eg --> Cucumber 50    (enter d when done)")

            else:
                print("INPUT FORMAT --> 'ITEM' WEIGHT (in gm) (default = 100)")
                print("          Eg --> Cucumber 50    (enter d when done)")
        else:
            # print(x[0])
            if x[1] == "":
                ratio = 1
            else:
                ratio = (int(x[1])) / 100

            if x[0] in d:
                l.append(x[0])
                c += d[x[0]][0] * ratio
                p += d[x[0]][1] * ratio
                f += d[x[0]][2] * ratio
                n += 1
            else:
                print("")
                print("Sorry the input item is not in our list , please input any other item")
                print("If you want to check the whole menu type (y/n)")
                t = input().lower()
                if t == "y":
                    datashow()
                    print("INPUT FORMAT --> 'ITEM' WEIGHT (in gm) (default = 100)")
                    print("          Eg --> Cucumber 50    (enter d when done)")
                else:
                    print("INPUT FORMAT --> 'ITEM' WEIGHT (in gm) (default = 100)")
                    print("          Eg --> Cucumber 50    (enter d when done)")
    sl = " , ".join(x for x in l)
    print("")
    print("")
    print("________________________________________________" + "_" * (len(sl) - 5))
    print(f"The items that you have selected are:  {sl}")
    # print("*All data is calculted per 100gm")
    print("________________________________________________" + "_" * (len(sl) - 5))
    print(f"Total calories :                       {round(c, 2)}")
    print("________________________________________________" + "_" * (len(sl) - 5))
    print(f"Total protein :                        {round(p, 2)}g")
    print("________________________________________________" + "_" * (len(sl) - 5))
    print(f"Total fats :                           {round(f, 2)}g")
    print("________________________________________________" + "_" * (len(sl) - 5))
    print("")
    print("")
    piecall(p, f)
    x = input("Enter to continue ")