from All_in_one_Cal import *


def personaldetailmenu(name, height, weight, age, gender):
    n = name
    h = height
    w = weight
    a = age
    g = gender
    youdetails(n, h, w, a, g)


def youdetails(name, height, weight, age, gender):
    print("=============================")
    print("        YOUR PROFILE         ")
    print("=============================")
    print("")
    bmi1 = BMI_Calculator(height, weight)
    # print("Your BMI is :",bmi1)
    # print("")
    BMI_Calculator_Result_Facts(bmi1)
    cal = Calories_calculate(height, weight, age, gender)
    print("")
    print("Calories required are :", cal)
    print("")
    male = ["male", "M", "m", "Male"]
    female = ["female", "F", "f", "Female"]
    if gender in male:
        Basal_Metabolic_Rate_Male(height, weight, age)
        print("")
        Body_Fat_Percentage_Male(height, weight, age)
        print("")
        Lean_Body_Mass_Male(height, weight)
        print("")
        x = (input("Enter to continue!"))
        print("")
    elif gender in female:
        Basal_Metabolic_Rate_Female(height, weight, age)
        print("")
        Body_Fat_Percentage_Female(height, weight, age)
        print("")
        Lean_Body_Mass_Female(height, weight)
        print("")
        x = (input("Enter to continue!"))
        print("")
    print("=============================")
