import matplotlib.pyplot as plt
import numpy as np


def graphcall(a, b, c, d):
    x = ['Breakfast', 'Lunch', 'Snacks', 'Dinner']
    y = [a, b, c, d]
    plt.bar(x, y, color=['#055c9d', '#003060', '#0e86d4', '#68bbe3'])
    plt.title('CALORIE DISTRIBUTION', fontdict={'fontname': 'DejaVu Sans', 'fontsize': 25})
    plt.xlabel('Meals', fontdict={'fontsize': 15})
    plt.ylabel('Calories', fontdict={'fontsize': 15})
    plt.xticks()
    plt.yticks()
    plt.show()


def piecall(p, f):
    if p == 0 or f == 0:
        pass
    else:
        if p >= f:
            y = np.array([p, f])
            mylabel = ['Protien', 'Fats']
            myexplode = [0.1, 0.1]
            mycolors = ['orange', 'royalblue']
            plt.pie(y, labels=mylabel, autopct='%.2f %%', explode=myexplode, shadow=True, colors=mycolors,
                    textprops={'fontname': 'Franklin Gothic Book', 'fontsize': 11})
            plt.title('Percentage Distribution', fontname='Franklin Gothic Book', fontsize=20)
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.04))
            plt.show()
        else:
            y = np.array([p, f])
            mylabel = ['Protien', 'Fats']
            myexplode = [0.1, 0.1]
            mycolors = ['orange', 'royalblue']
            plt.pie(y, labels=mylabel, autopct='%.2f %%', explode=myexplode, shadow=True, colors=mycolors,
                    textprops={'fontname': 'Franklin Gothic Book', 'fontsize': 11})
            plt.title('Percentage Distribution', fontname='Franklin Gothic Book', fontsize=20)
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.04))
            plt.show()
