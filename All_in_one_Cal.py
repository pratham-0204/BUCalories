def get_weight():
    person_weight = (input("Enter your weight in kilograms: "))
    while True:
        x = ""
        lst = ['~', '`', '!', '@', '#', '$', '%', '^', '*', '&', '()', '(', ')', '<', '>', '-', '+', '*', '/', '?', '/',
               ',']
        for i in person_weight:
            if i != " " and i != ".":
                x += i
        if person_weight == "":
            person_weight = (
                input("                                            └►Invalid input \nEnter your weight in kilograms: "))
        elif x in lst:
            person_weight = input("                                └►Invalid input \nEnter your weight in kilograms: ")
        elif x.isalpha() or float(person_weight) <= 0:
            person_weight = (
                input("                                            └►Invalid input \nEnter your weight in kilograms: "))
        elif x.isdigit():
            return float(person_weight)
        else:
            person_weight = (input("                               └►Invalid input \nEnter your weight in kilograms: "))


def get_height():
    person_height = input("Enter your height in Meters: ")
    while True:
        x = ""
        lst = ['~', '`', '!', '@', '#', '$', '%', '^', '*', '&', '()', '(', ')', '<', '>', '-', '+', '*', '/', '?', '/',
               ',']
        for i in person_height:
            if i != " " and i != ".":
                x += i
        if person_height == "":
            person_height = input("                             └►Invalid input \nEnter your height in Meters: ")
        elif x in lst:
            person_height = input("                             └►Invalid input \nEnter your height in Meters: ")
        elif x.isalpha() or float(person_height) <= 0:
            person_height = input("                             └►Invalid input \nEnter your height in Meters: ")
        elif x.isdigit():
            return float(person_height)
        else:
            person_height = (input("                            └►Invalid input \nEnter your height in Meters: "))


def sex():
    sexes = ["male", "female", "M", "F", "f", "m", "Male", "Female"]
    while True:
        gender = str(input("Do you identify as male or female? "))
        while gender not in sexes:
            gender = str(
                input("                                   └►Invalid input \nDo you identify as male or female? "))
        else:
            return gender


def get_age():
    Age = (input("Enter your age in years: "))
    while True:
        x = ""
        lst = ['~', '`', '!', '@', '#', '$', '%', '^', '*', '&', '()', '(', ')', '<', '>', '-', '+', '*', '/', '?', '/',
               ',', '. ']
        for i in Age:
            if i != " " and i != ".":
                x += i
        if Age == "":
            Age = (input("                         └►Invalid input \nEnter your age in years: "))
        elif x in lst:
            Age = (input("                         └►Invalid input \nEnter your age in years: "))
        elif x.isalpha() or float(Age) <= 0:
            Age = (input("                         └►Invalid input \nEnter your age in years: "))
        elif x.isdigit():
            return int(Age)
        else:
            Age = (input("                         └►Invalid input \nEnter your age in years: "))


def BMI_Calculator(person_height, person_weight):
    # HEIGHT(m) , WEIGHT(kg)
    BMI = person_weight / person_height ** 2
    return round(BMI, 2)


def BMI_Calculator_Result_Facts(BMI):
    #    BMI = person_weight / person_height ** 2
    #    BMI_result = round(BMI, 2)
    s = " "
    ds = str(round(BMI, 2))
    BMI_result = BMI
    print(
        "------------------------------------------------------------------------------------------------------------------------")
    print(
        ":           BMI           :         CATEGORY         :    EXERCISES     :                   TIPS                       :")
    print(
        "------------------------------------------------------------------------------------------------------------------------")
    if BMI_result <= 18.4:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:    You are underweight   :    Walking       :   Drink 6-8 glasses of distilled water a day :")
        print(
            ":                         :                          :    Jogging       :   Eat frequent but small meals               :")
        print(
            ":                         :                          :    Yoga          :   Do not eat processed foods                 :")
        print(
            ":                         :                          :    Sit-ups       :   Reduce intake of dairy products            :")
        print(
            ":                         :                          :    Squats        :   Avoid red meat and animal fats             :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")
    elif BMI_result <= 24.9:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:     You are healthy      :     Running      :        keep doing what you are doing :)      :")
        print(
            ":                         :                          :     Pushups      :                                              :")
        print(
            ":                         :                          :     Lunges       :                                              :")
        print(
            ":                         :                          :  Bicep Training  :                                              :")
        print(
            ":                         :                          :     Pullups      :                                              :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")
    elif BMI_result <= 29.9:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:    You are over weight   :    Swimming      :   Cut out fried foods                        :")
        print(
            ":                         :                          :    Burpees       :   Start with a soup or a salad               :")
        print(
            ":                         :                          :    Jump rope     :   Drink 8 glasses of distilled water a day   : ")
        print(
            ":                         :                          :    Side planks   :   Reduce intake of dairy products            :")
        print(
            ":                         :                          :    Treadmill     :   Avoid red meat and animal fats             :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")
    elif BMI_result <= 34.9:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:    You are corpulent     :   Swimming       :   Cut out fried foods                        :")
        print(
            ":                         :                          :   Wall pushups   :   Drink 9 glasses of distilled water a day   :")
        print(
            ":                         :                          :   Calf raises    :   Avoid red meat and animal fats             :")
        print(
            ":                         :                          :   Knee hugs      :   Reduce intake of dairy products            :")
        print(
            ":                         :                          :   Boxing         :   Start with a soup or a salad               :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")
    elif BMI_result <= 39.9:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:       You are obese      :   Swimming       :   Cut out fried foods                        :")
        print(
            ":                         :                          :   Wall pushups   :   Drink 9 glasses of distilled water a day   :")
        print(
            ":                         :                          :   Calf raises    :   Avoid red meat and animal fats             :")
        print(
            ":                         :                          :   Knee hugs      :   Reduce intake of dairy products            :")
        print(
            ":                         :                          :   Boxing         :   Start with a soup or a salad               :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")
    else:
        print(
            f":{s * 10}{BMI_result}{s * (15 - len(ds))}:  You are severely obese  :   Swimming       :   Cut out fried foods                        :")
        print(
            ":                         :                          :   Wall pushups   :   Drink 9 glasses of distilled water a day   :")
        print(
            ":                         :                          :   Calf raises    :   Avoid red meat and animal fats             :")
        print(
            ":                         :                          :   Knee hugs      :   Reduce intake of dairy products            :")
        print(
            ":                         :                          :   Side crunches  :   Start with a soup or a salad               :")
        print(
            "------------------------------------------------------------------------------------------------------------------------")


def Calories_calculate(person_height, person_weight, Age, gender):
    male = ["male", "M", "m", "Male"]
    # female = ["female", "F", "f", "Female"]
    if gender in male:
        CC = 66 + (12.7 * person_weight) + (6.23 * (person_height * 100)) - (6.8 * Age)
        return round(CC, 2)
    else:
        CC = 655 + (4.35 * person_weight) + (4.7 * (person_height * 100)) - (4.7 * Age)
        return round(CC, 2)


def Basal_Metabolic_Rate_Male(person_height, person_weight, Age):
    BMR_M = 88.362 + (13.397 * person_weight) + (4.799 * (person_height * 100) - (5.677 * Age))
    print("---------------------------------------------------------------")
    print(":             TOTAL DAILY CALORIES NEEDS       :     BMR      :")
    print("---------------------------------------------------------------")
    print(":             Your basal metabolic rate(BMR)   :   ", "%.2f" % BMR_M, "  :")
    print(":          Sedentary (little or no exercise)   :   ", "%.2f" % (BMR_M * 1.2), "  :")
    print(":      Lightly Active (sports 1-3 days/week)   :   ", "%.2f" % (BMR_M * 1.375), "  :")
    print(":   Moderately Active (sports 3-5 days/week)   :   ", "%.2f" % (BMR_M * 1.55), "  :")
    print(":       Very Active (sports 6-7 days a week)   :   ", "%.2f" % (BMR_M * 1.725), "  :")
    print(":       Extra Active (sports & physical job)   :   ", "%.2f" % (BMR_M * 1.9), "  :")
    print("---------------------------------------------------------------")
    print("\n")


def Basal_Metabolic_Rate_Female(person_height, person_weight, Age):
    BMR_F = 447.593 + (9.247 * person_weight) + (3.098 * (person_height * 100) - (4.330 * Age))
    print("---------------------------------------------------------------")
    print(":             TOTAL DAILY CALORIES NEEDS       :     BMR      :")
    print("---------------------------------------------------------------")
    print(":             Your basal metabolic rate(BMR)   :   ", "%.2f" % BMR_F, "  :")
    print(":          Sedentary (little or no exercise)   :   ", "%.2f" % (BMR_F * 1.2), "   :")
    print(":      Lightly Active (sports 1-3 days/week)   :   ", "%.2f" % (BMR_F * 1.375), "  :")
    print(":   Moderately Active (sports 3-5 days/week)   :   ", "%.2f" % (BMR_F * 1.55), "  :")
    print(":       Very Active (sports 6-7 days a week)   :   ", "%.2f" % (BMR_F * 1.725), "   :")
    print(":       Extra Active (sports & physical job)   :   ", "%.2f" % (BMR_F * 1.9), "  :")
    print("---------------------------------------------------------------")
    print("\n")


def Body_Fat_Percentage_Male(person_height, person_weight, Age):
    BMI = (person_weight / person_height ** 2)
    BFP_M = (1.20 * BMI) + (0.238 * Age) - 16.2
    print("\n● Your body fat percentage is:", round(BFP_M, 2))
    if 2 >= BFP_M <= 4:
        print("                                 └► You are in essential fat category")
    elif 6 >= BFP_M <= 13:
        print("                                 └► You are in athletic category")
    elif 14 >= BFP_M <= 17:
        print("                                 └► You are in fitness category")
    elif 18 >= BFP_M <= 25:
        print("                                 └► You are in average category")
    elif BFP_M >= 26:
        print("                                 └► You are in obese category")


def Body_Fat_Percentage_Female(person_height, person_weight, Age):
    BMI = (person_weight / person_height ** 2)
    BFP_F = (1.20 * BMI) + (0.238 * Age) - 5.4
    print("\n● Your body fat percentage is:", BFP_F)
    if 10 >= BFP_F <= 12:
        print("                                 └► You are in essential fat category")
    elif 14 >= BFP_F <= 20:
        print("                                 └► You are in athletic category")
    elif 21 >= BFP_F <= 24:
        print("                                 └► You are in fitness category")
    elif 25 >= BFP_F <= 31:
        print("                                 └► You are in average category")
    elif BFP_F >= 32:
        print("                                 └► You are in obese category")


def Lean_Body_Mass_Male(person_height, person_weight):
    LBM_M = (0.407 * person_weight) + (0.267 * (person_height * 100) - 19.2)
    print("\n● Your lean body mass is:", round(LBM_M, 2), "%")


def Lean_Body_Mass_Female(person_height, person_weight):
    LBM_F = (0.252 * person_weight) + (0.473 * (person_height * 100) - 48.3)
    print("\n● Your lean body mass is:", round(LBM_F, 2), "%")
