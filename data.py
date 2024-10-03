from ctypes.wintypes import LPWIN32_FIND_DATAA
from random import *


def data():
    d = {
        'veg in hot garlic sauce': (176.4, 5.2, 33.8),
        'palak paneer': (183, 10.6, 24),
        'phirni': (122.3, 9.3, 13),
        'fruit custard': (83.3, 6.5, 7.7),
        'mix veg raita': (39.5, 2.3, 6.2),
        'arhar dal': (187, 22, 1.5),
        'kimchi salad': (97.4, 1.7, 7.9),
        'rajma': (100.8, 24, 0.8),
        'sweet corn soup': (49, 1.6, 0.3),
        'veg kofta curry': (103.3, 9, 15),
        'kala chana': (163, 20, 6),
        'veg poriyal': (91, 2.7, 5.1),
        'soya chap masala': (100, 9.5, 1.25),
        'chana dal': (138.6, 21.6, 4.5),
        'sindhi kadi': (69, 7, 12.2),
        'black masoori dal': (350.4, 9, 0.4),
        'coconut chutney': (163, 3.58, 33.2),
        'baigan bharta': (97, 0.9, 2.4),
        'paneer lababdar': (189, 5.5, 12.8),
        'gobhi aloo': (72.2, 2.5, 5.6),
        'sewaiyan kheer': (244.3, 10, 12),
        'channa dal tadka': (140, 10, 2.14),
        'green salad': (23.2, 1.5, 0.24),
        'subz miloni': (83, 6, 1),
        'dal tadka': (129.5, 6.2, 4.2),
        'kadahi veg': (89, 1, 7.4),
        'onion': (44.3, 1.1, 0.1),
        'gr. cheese sandwich': (315, 9.16, 15.77),
        'mix fruit': (53, 1.4, 0.5),
        'palak corn': (98, 2.94, 2.04),
        'burani raita': (39.5, 1.45, 2.15),
        'pao': (210, 9, 3.2),
        'bhaji': (101.2, 5.5, 1.3),
        'shahi tukda': (396, 7, 17),
        'veg pulao': (126, 3.2, 1.6),
        'steamed rice': (133.3, 2.8, 0.3),
        'mix veg paratha': (335.4, 6, 7),
        'cream of spinach soup': (80.6, 3, 4.8),
        'chana dal tadka': (140, 7, 2.5),
        'makhani': (170.3, 6.5, 9.5),
        'malai kofta curry': (217, 6, 9.5),
        'choley amritsari': (170, 4, 8),
        'lauki kofta curry': (110, 3.1, 5.6),
        'poha': (110, 2, 0.12),
        'mooli': (16, 0.7, 0.1),
        'roti': (300, 7.8, 9.3),
        'green chutney': (14, 5, 8.2),
        'sweet chutney': (149, 0.6, 0.2),
        'gobi matar': (130, 4, 8),
        'gajar matar methi': (123, 2.5, 5.5),
        'khatta meetha petha': (300, 0.5, 0.2),
        'dum aloo kashmiri': (170, 1.8, 6.4),
        'tomato basil soup': (44, 1, 1.4),
        'besan ladoo': (500, 10, 24.6),
        'stuffed kulcha': (221, 4.8, 4.8),
        'jeera rice': (204, 6.22, 4.73),
        'orange': (49, 0.9, 0.2),
        'chocos': (387, 19, 3),
        'tomato rice': (110.8, 1.8, 3.1),
        'soya masala dry': (346, 52.3, 0),
        'achari aloo': (125, 2, 5),
        'moth dal': (340, 23, 1.6),
        'mix dal': (354, 23.22, 1.96),
        'sambar': (52, 2.8, 0.3),
        'poha with vegetables': (110, 2, 0.2),
        'bhelpuri': (202, 6.5, 10.1),
        'aloo shimla mirch': (133, 2.34, 2.9),
        'mexican veg': (92, 2.5, 5),
        'boiled egg': (156, 12.6, 10.6),
        'curd': (62, 5.3, 1.6),
        'dal panchmail': (190, 9, 4.4),
        'green moong dal': (118, 8, 1),
        'idli': (150, 4.2, 1.1),
        'mirchi salan': (219, 5, 18),
        'nutri pulav (white rice)': (140, 14, 5.5),
        'sirka onion': (42, 1.2, 8.8),
        'aloo palak dry': (116, 2, 7),
        'egg curry': (114, 5.9, 7.11),
        'sweet milk daliya': (122.74, 2.2, 1.5),
        'coffee': (17, 0.12, 0.02),
        'rajma': (333, 8.7, 0.5),
        'vermicelli kheer': (244.13, 3.06, 1.9),
        'besan burfi': (648, 13.1, 4.5),
        'masala idli': (174, 9, 8),
        'egg biryani': (131.3, 6.7, 7.9),
        'cream of cauliflower soup': (52, 3, 4.7),
        'onion rice': (172, 3, 1.1),
        'adraki rassam': (66.5, 1.1, 1.6),
        'veg uttapam': (181, 4.5, 5.6),
        'yellow dal tadka': (149, 9, 6),
        'milk': (42, 3.4, 1),
        'tamatar dhaniya ka shorba': (94, 11.5, 12.5),
        'veg clear soup': (32, 1.7, 1.9),

        'veg kofta': (143.7, 13.4, 19.7),
        'mooli cream of spinach': (74, 3.5, 5),
        'nimbu pani': (40, 0.1, 0.3),
        'banana': (89, 1.1, 0.3),
        'urad chilka dal': (350, 23, 1.4),
        'veg jalfrezi': (86, 1, 4),
        'white bread': (265, 9, 3.2),
        'mattar paneer': (121.5, 6.3, 9.1),
        'cabbage matar': (25, 1, 2.8),
        'dal bukhara': (121, 5, 5.3),
        'atta halwa': (186, 2.8, 6.5),
        'mattar kulcha': (450, 19, 10),
        'gobi paratha': (254, 5, 11.4),
        'cornflakes': (357, 8, 0.4),
        'vada': (217, 6.5, 8.5),
        'jam': (278, 0.4, 0.1),
        'cheese grilled sandwich': (315, 11, 19),
        'kadai soya': (340, 11, 3),
        'ajwaini poori': (296, 8.3, 23.1),
        'gobi adraki': (30, 2.2, 3.5),
        'bagare baigan': (138.8, 2.4, 7.8),
        'sarson ka saag': (239, 1.3, 8),
        'moong sprouts': (30, 3.4, 0.3),
        'veg masala macaroni': (161, 4.52, 0.11),
        'cheese corn sandwich': (172, 5.7, 35.7),
        'veg korma dal': (133.9, 2.8, 4.4),
        'veg oats': (90, 13.1, 6.5),
        'aloo pyaz paratha': (98, 2.4, 6),
        'dahi papdi': (189, 6.8, 10),
        'custard': (122, 4, 4),
        'sewayian upma': (164.1, 3.9, 5.4),
        'tea': (17, 0.5, 0.4),
        'paratha': (325, 6.4, 11.2),
        'methi dal': (175, 6, 2),
        'samosa': (308, 4.6, 17.8),
        'raita': (46, 5, 3.6, 3.1),
        'tomato ketchup': (112, 1.3, 0.2),
        'aloo palak': (93, 2.8, 3.8),
        'veg. daliya': (357, 12, 1.3),
        'veg biryani': (130, 3.1, 2.5),
        'kheera raita': (60, 3.6, 3.1),
        'boondi raita': (113, 5.13, 5.75),
        'manchow soup': (420, 7, 4.2),
        'brown bread': (313, 13, 4.3),
        'veg noodles': (121, 5, 2.5),
        'gatta curry': (110, 5.4, 16),
        'paneer butter masala': (211, 9.2, 16.6),
        'masala roti': (340, 10, 12),
        'bread pakoda': (283, 12.4, 4.9),
        'cucumber': (15, 2, 0.1),
        'veg fried rice': (163, 4.7, 2.3),
        'hot n sour soup': (39, 2.6, 1.2),
        'laccha onion': (44, 2, 4),
        'nutri keema': (155, 52, 7.9),
        'curry': (103.3, 9, 15),
        'curry lobiya masala': (115, 8, 3.2),
        'kadhai veg paneer': (189, 5.5, 12.8),
        'malai kofta': (217, 6, 9.5),
        'aloo pyaz': (98, 2.4, 6),
        'dry rajma': (333, 8.7, 0.5)

    }
    return d


def datakeylist():
    l = []
    d = data()
    for i in d:
        l.append(i)
    print(l)


# datalist()

def datalist():
    l = [
        ['hot garlic sauce', 176.4, 5.2, 33.8],
        ['palak paneer', 183, 10.6, 24],
        ['phirni', 122.3, 9.3, 13],
        ['fruit custard', 83.3, 6.5, 7.7],
        ['mix veg raita', 39.5, 2.3, 6.2],
        ['arhar dal', 187, 22, 1.5],
        ['kimchi salad', 97.4, 1.7, 7.9],
        ['rajma', 100.8, 24, 0.8],
        ['sweet corn soup', 49, 1.6, 0.3],
        ['curry', 103.3, 9, 15],
        ['kala chana', 163, 20, 6],
        ['veg poriyal', 91, 2.7, 5.1],
        ['soya chap masala', 100, 9.5, 1.25],
        ['chana dal', 138.6, 21.6, 4.5],
        ['sindhi kadi', 69, 7, 12.2],
        ['black masoori dal', 350.4, 9, 0.4],
        ['coconut chutney', 163, 3.58, 33.2],
        ['baigan bharta', 97, 0.9, 2.4],
        ['kadhai veg paneer', 189, 5.5, 12.8],
        ['gobhi aloo', 72.2, 2.5, 5.6],
        ['sewaiyan kheer', 244.3, 10, 12],
        ['channa dal tadka', 140, 10, 2.14],
        ['green salad', 23.2, 1.5, 0.24],
        ['subz miloni', 83, 6, 1],
        ['dal tadka', 129.5, 6.2, 4.2],
        ['kadahi veg', 89, 1, 7.4],
        ['onion', 44.3, 1.1, 0.1],
        ['gr. cheese sandwich', 315, 9.16, 15.77],
        ['mix fruit', 53, 1.4, 0.5],
        ['palak corn', 98, 2.94, 2.04],
        ['burani raita', 39.5, 1.45, 2.15],
        ['pao', 210, 9, 3.2],
        ['bhaji', 101.2, 5.5, 1.3],
        ['shahi tukda', 396, 7, 17],
        ['veg pulao', 126, 3.2, 1.6],
        ['steamed rice', 133.3, 2.8, 0.3],
        ['mix veg paratha', 335.4, 6, 7],
        ['cream of spinach soup', 80.6, 3, 4.8],
        ['chana dal tadka', 140, 7, 2.5],
        ['makhani', 170.3, 6.5, 9.5],
        ['malai kofta', 217, 6, 9.5],
        ['choley amritsari', 170, 4, 8],
        ['lauki kofta curry', 110, 3.1, 5.6],
        ['poha', 110, 2, 0.12],
        ['mooli', 16, 0.7, 0.1],
        ['roti', 300, 7.8, 9.3],
        ['green chutney', 14, 5, 8.2],
        ['sweet chutney', 149, 0.6, 0.2],
        ['gobi matar', 130, 4, 8],
        ['gajar matar methi', 123, 2.5, 5.5],
        ['khatta meetha petha', 300, 0.5, 0.2],
        ['dum aloo kashmiri', 170, 1.8, 6.4],
        ['tomato basil soup', 44, 1, 1.4],
        ['besan ladoo', 500, 10, 24.6],
        ['stuffed kulcha', 221, 4.8, 4.8],
        ['jeera rice', 204, 6.22, 4.73],
        ['orange', 49, 0.9, 0.2],
        ['chocos', 387, 19, 3],
        ['tomato rice', 110.8, 1.8, 3.1],
        ['soya masala dry', 346, 52.3, 0.5],
        ['achari aloo', 125, 2, 5],
        ['moth dal', 340, 23, 1.6],
        ['mix dal', 354, 23.22, 1.96],
        ['sambar', 52, 2.8, 0.3],
        ['poha with vegetables', 110, 2, 0.2],
        ['bhelpuri', 202, 6.5, 10.1],
        ['aloo shimla mirch', 133, 2.34, 2.9],
        ['mexican veg', 92, 2.5, 5],
        ['boiled egg', 156, 12.6, 10.6],
        ['curd', 62, 5.3, 1.6],
        ['dal panchmail', 190, 9, 4.4],
        ['green moong dal', 118, 8, 1],
        ['idli', 150, 4.2, 1.1],
        ['mirchi salan', 219, 5, 18],
        ['nutri pulao (white rice)', 140, 14, 5.5],
        ['sirka onion', 42, 1.2, 8.8],
        ['aloo palak dry', 116, 2, 7],
        ['egg curry', 114, 5.9, 7.11],
        ['sweet milk daliya', 122.74, 2.2, 1.5],
        ['coffee', 17, 0.12, 0.02],
        ['dry rajma', 333, 8.7, 0.5],
        ['vermicelli kheer', 244.13, 3.06, 1.9],
        ['besan burfi', 648, 13.1, 4.5],
        ['masala idli', 174, 9, 8],
        ['egg biryani', 131.3, 6.7, 7.9],
        ['cream of cauliflower soup', 52, 3, 4.7],
        ['onion rice', 172, 3, 1.1],
        ['adraki rassam', 66.5, 1.1, 1.6],
        ['veg uttapam', 181, 4.5, 5.6],
        ['yellow dal tadka', 149, 9, 6],
        ['milk', 42, 3.4, 1],
        ['tamatar dhaniya ka shorba', 94, 11.5, 12.5],
        ['veg clear soup', 32, 1.7, 1.9],
        ['choley amritsari', 170, 3, 6],
        ['veg kofta', 143.7, 13.4, 19.7],
        ['mooli cream of spinach', 74, 3.5, 5],
        ['nimbu pani', 40, 0.1, 0.3],
        ['banana', 89, 1.1, 0.3],
        ['urad chilka dal', 350, 23, 1.4],
        ['veg jalfrezi', 86, 1, 4],
        ['white bread', 265, 9, 3.2],
        ['mattar paneer', 121.5, 6.3, 9.1],
        ['cabbage matar', 25, 1, 2.8],
        ['dal bukhara', 121, 5, 5.3],
        ['atta halwa', 186, 2.8, 6.5],
        ['mattar kulcha', 450, 19, 10],
        ['gobi paratha', 254, 5, 11.4],
        ['cornflakes', 357, 8, 0.4],
        ['vada', 217, 6.5, 8.5],
        ['jam', 278, 0.4, 0.1],
        ['cheese grilled sandwich', 315, 11, 19],
        ['kadai soya', 340, 11, 3],
        ['ajwaini poori', 296, 8.3, 23.1],
        ['gobi adraki', 30, 2.2, 3.5],
        ['bagare baigan', 138.8, 2.4, 7.8],
        ['sarson ka saag', 239, 1.3, 8],
        ['moong sprouts', 30, 3.4, 0.3],
        ['veg masala macaroni', 161, 4.52, 0.11],
        ['cheese corn sandwich', 172, 5.7, 35.7],
        ['veg korma dal', 133.9, 2.8, 4.4],
        ['veg oats', 90, 13.1, 6.5],
        ['aloo pyaz', 98, 2.4, 6],
        ['dahi papdi', 189, 6.8, 10],
        ['custard', 122, 4, 4],
        ['sewayian upma', 164.1, 3.9, 5.4],
        ['tea', 17, 0.5, 0.4],
        ['paratha', 325, 6.4, 11.2],
        ['methi dal', 175, 6, 2],
        ['samosa', 308, 4.6, 17.8],
        ['raita', 46, 5, 3.6, 3.1],
        ['tomato ketchup', 112, 1.3, 0.2],
        ['aloo palak', 93, 2.8, 3.8],
        ['veg. daliya', 357, 12, 1.3],
        ['veg biryani', 130, 3.1, 2.5],
        ['kheera raita', 60, 3.6, 3.1],
        ['boondi raita', 113, 5.13, 5.75],
        ['manchow soup', 420, 7, 4.2],
        ['brown bread', 313, 13, 4.3],
        ['veg noodles', 121, 5, 2.5],
        ['gatta curry', 110, 5.4, 16],
        ['paneer butter masala', 211, 9.2, 16.6],
        ['masala roti', 340, 10, 12],
        ['bread pakoda', 283, 12.4, 4.9],
        ['cucumber', 15, 2, 0.1],
        ['veg fried rice', 163, 4.7, 2.3],
        ['hot n sour soup', 39, 2.6, 1.2],
        ['laccha onion', 44, 2, 4]
    ]
    return l


def Breakfast():
    l1 = [
        ['brown bread', 313, 13, 4.3],
        ['veg. daliya', 357, 12, 1.3],
        ['tomato ketchup', 112, 1.3, 0.2],
        ['paratha', 325, 6.4, 11.2],
        ['tea', 17, 0.5, 0.4],
        ['coconut chutney', 163, 3.58, 33.2],
        ['sewayian upma', 164.1, 3.9, 5.4],
        ['aloo pyaz paratha', 98, 2.4, 6],
        ['veg oats', 90, 13.1, 6.5],
        ['cheese corn sandwich', 172, 5.7, 35.7],
        ['gr. cheese sandwich', 315, 9.16, 15.77],
        ['mix fruit', 53, 1.4, 0.5],
        ['ajwaini poori', 296, 8.3, 23.1],
        ['cheese grilled sandwich', 315, 11, 19],
        ['jam', 278, 0.4, 0.1],
        ['vada', 217, 6.5, 8.5],
        ['cornflakes', 357, 8, 0.4],
        ['gobi paratha', 254, 5, 11.4],
        ['mattar kulcha', 450, 19, 10],
        ['pao', 210, 9, 3.2],
        ['bhaji', 101.2, 5.5, 1.3],
        ['white bread', 265, 9, 3.2],
        ['mix veg paratha', 335.4, 6, 7],
        ['banana', 89, 1.1, 0.3],
        ['milk', 42, 3.4, 1],
        ['veg uttapam', 181, 4.5, 5.6],
        ['khatta meetha petha', 300, 0.5, 0.2],
        ['orange', 49, 0.9, 0.2],
        ['chocos', 387, 19, 3],
        ['coffee', 17, 0.12, 0.02],
        ['sweet milk daliya', 122.74, 2.2, 1.5],
        ['boiled egg', 156, 12.6, 10.6],
        ['idli', 150, 4.2, 1.1]
    ]
    return l1


def Lunch():
    l2 = [
        ['hot garlic sauce', 176.4, 5.2, 33.8],
        ['veg fried rice', 163, 4.7, 2.3],
        ['paneer butter masala', 211, 9.2, 16.6],
        ['boondi raita', 113, 5.13, 5.75],
        ['kheera raita', 60, 3.6, 3.1],
        ['veg biryani', 130, 3.1, 2.5],
        ['mix veg raita', 39.5, 2.3, 6.2],
        ['aloo palak', 93, 2.8, 3.8],
        ['kimchi salad', 97.4, 1.7, 7.9],
        ['rajma', 100.8, 24, 0.8],
        ['raita', 46, 5, 3.6, 3.1],
        ['soya chap masala', 100, 9.5, 1.25],
        ['chana dal', 138.6, 21.6, 4.5],
        ['sindhi kadi', 69, 7, 12.2],
        ['baigan bharta', 97, 0.9, 2.4],
        ['paneer lababdar', 189, 5.5, 12.8],
        ['gobhi aloo', 72.2, 2.5, 5.6],
        ['green salad', 23.2, 1.5, 0.24],
        ['subz miloni', 83, 6, 1],
        ['veg korma dal', 133.9, 2.8, 4.4],
        ['dal tadka', 129.5, 6.2, 4.2],
        ['kadahi veg', 89, 1, 7.4],
        ['onion', 44.3, 1.1, 0.1],
        ['moong sprouts', 30, 3.4, 0.3],
        ['kadai soya', 340, 11, 3],
        ['methi dal', 175, 6, 2],
        ['dal bukhara', 121, 5, 5.3],
        ['burani raita', 39.5, 1.45, 2.15],
        ['veg pulao', 126, 3.2, 1.6],
        ['steamed rice', 133.3, 2.8, 0.3],
        ['mattar paneer', 121.5, 6.3, 9.1],
        ['veg jalfrezi', 86, 1, 4],
        ['urad chilka dal', 350, 23, 1.4],
        ['makhani', 170.3, 6.5, 9.5],
        ['malai kofta curry', 217, 6, 9.5],
        ['roti', 300, 7.8, 9.3],
        ['yellow dal tadka', 149, 9, 6],
        ['jeera rice', 204, 6.22, 4.73],
        ['egg biryani', 131.3, 6.7, 7.9],
        ['achari aloo', 125, 2, 5],
        ['rajma', 333, 8.7, 0.5],
        ['mix dal', 354, 23.22, 1.96],
        ['sambar', 52, 2.8, 0.3],
        ['egg curry', 114, 5.9, 7.11],
        ['aloo palak dry', 116, 2, 7],
        ['sirka onion', 42, 1.2, 8.8],
        ['curd', 62, 5.3, 1.6],
        ['dal panchmail', 190, 9, 4.4],
        ['nutri pulav (white rice)', 140, 14, 5.5],
        ['green moong dal', 118, 8, 1],
        ['mirchi salan', 219, 5, 18]
    ]
    return l2


def snacks():
    l3 = [
        ['bread pakoda', 283, 12.4, 4.9],
        ['veg noodles', 121, 5, 2.5],
        ['tomato ketchup', 112, 1.3, 0.2],
        ['samosa', 308, 4.6, 17.8, ],
        ['tea', 17, 0.5, 0.4],
        ['dahi papdi', 189, 6.8, 10],
        ['veg masala macaroni', 161, 4.52, 0.11],
        ['gr. cheese sandwich', 315, 9.16, 15.77],
        ['cheese grilled sandwich', 315, 11, 19],
        ['poha', 110, 2, 0.12],
        ['green chutney', 14, 5, 8.2],
        ['sweet chutney', 149, 0.6, 0.2],
        ['stuffed kulcha', 221, 4.8, 4.8],
        ['masala idli', 174, 9, 8],
        ['coffee', 17, 0.12, 0.02],
        ['poha with vegetables', 110, 2, 0.2],
        ['bhelpuri', 202, 6.5, 10.1]
    ]
    return l3


def dinner():
    l4 = [
        ['laccha onion', 44, 2, 4],
        ['hot n sour soup', 39, 2.6, 1.2],
        ['palak paneer', 183, 10.6, 24],
        ['cucumber', 15, 2, 0.1],
        ['phirni', 122.3, 9.3, 13],
        ['fruit custard', 83.3, 6.5, 7.7],
        ['masala roti', 340, 10, 12],
        ['paneer butter masala', 211, 9.2, 16.6],
        ['gatta curry', 110, 5.4, 16],
        ['manchow soup', 420, 7, 4.2],
        ['arhar dal', 187, 22, 1.5],
        ['sweet corn soup', 49, 1.6, 0.3],
        ['veg kofta curry', 103.3, 9, 15],
        ['kala chana', 163, 20, 6],
        ['veg poriyal', 91, 2.7, 5.1],
        ['black masoori dal', 350.4, 9, 0.4],
        ['custard', 122, 4, 4],
        ['sewaiyan kheer', 244.3, 10, 12],
        ['channa dal tadka', 140, 10, 2.14],
        ['onion', 44.3, 1.1, 0.1],
        ['sarson ka saag', 239, 1.3, 8],
        ['palak corn', 98, 2.94, 2.04],
        ['bagare baigan', 138.8, 2.4, 7.8],
        ['gobi adraki', 30, 2.2, 3.5],
        ['kadai soya', 340, 11, 3],
        ['atta halwa', 186, 2.8, 6.5],
        ['dal bukhara', 121, 5, 5.3],
        ['shahi tukda', 396, 7, 17],
        ['cabbage matar', 25, 1, 2.8],
        ['cream of spinach soup', 80.6, 3, 4.8],
        ['chana dal tadka', 140, 7, 2.5],
        ['mooli cream of spinach', 74, 3.5, 5],
        ['choley amritsari', 170, 4, 8],
        ['veg kofta', 143.7, 13.4, 19.7],
        ['veg clear soup', 32, 1.7, 1.9],
        ['lauki kofta curry', 110, 3.1, 5.6],
        ['tamatar dhaniya ka shorba', 94, 11.5, 12.5],
        ['mooli', 16, 0.7, 0.1],
        ['roti', 300, 7.8, 9.3],
        ['adraki rassam', 66.5, 1.1, 1.6],
        ['gobi matar', 130, 4, 8],
        ['gajar matar methi', 123, 2.5, 5.5],
        ['onion rice', 172, 3, 1.1],
        ['cream of cauliflower soup', 52, 3, 4.7],
        ['dum aloo kashmiri', 170, 1.8, 6.4],
        ['tomato basil soup', 44, 1, 1.4],
        ['besan ladoo', 500, 10, 24.6],
        ['jeera rice', 204, 6.22, 4.73],
        ['tomato rice', 110.8, 1.8, 3.1],
        ['besan burfi', 648, 13.1, 4.5],
        ['soya masala dry', 346, 52.3, 0.5],
        ['vermicelli kheer', 244.13, 3.06, 1.9],
        ['moth dal', 340, 23, 1.6],
        ['egg curry', 114, 5.9, 7.11],
        ['aloo shimla mirch', 133, 2.34, 2.9],
        ['mexican veg', 92, 2.5, 5, ]
    ]
    return l4


def dishes():
    l = [
        ['palak paneer', 183, 10.6, 24],

        ['arhar dal', 187, 22, 1.5],

        ['veg kofta curry', 103.3, 9, 15],

        ['kala chana', 163, 20, 6],

        ['veg poriyal', 91, 2.7, 5.1],

        ['soya chap masala', 100, 9.5, 1.25],

        ['chana dal', 138.6, 21.6, 4.5],

        ['sindhi kadi', 69, 7, 12.2],

        ['black masoori dal', 350.4, 9, 0.4],

        ['baigan bharta', 97, 0.9, 2.4],

        ['paneer lababdar', 189, 5.5, 12.8],

        ['gobhi aloo', 72.2, 2.5, 5.6],

        ['channa dal tadka', 140, 10, 2.14],

        ['subz miloni', 83, 6, 1],

        ['dal tadka', 129.5, 6.2, 4.2],

        ['kadahi veg', 89, 1, 7.4],

        ['palak corn', 98, 2.94, 2.04],

        ['bhaji', 101.2, 5.5, 1.3],

        ['chana dal tadka', 140, 7, 2.5],

        ['makhani', 170.3, 6.5, 9.5],

        ['malai kofta curry', 217, 6, 9.5],

        ['choley amritsari', 170, 4, 8],

        ['lauki kofta curry', 110, 3.1, 5.6],

        ['gobi matar', 130, 4, 8],

        ['gajar matar methi', 123, 2.5, 5.5],

        ['khatta meetha petha', 300, 0.5, 0.2],

        ['dum aloo kashmiri', 170, 1.8, 6.4],

        ['soya masala dry', 346, 52.3, 0],

        ['achari aloo', 125, 2, 5],

        ['moth dal', 340, 23, 1.6],

        ['mix dal', 354, 23.22, 1.96],

        ['sambar', 52, 2.8, 0.3],

        ['mexican veg', 92, 2.5, 5],

        ['dal panchmail', 190, 9, 4.4],

        ['green moong dal', 118, 8, 1],

        ['aloo palak dry', 116, 2, 7],

        ['rajma', 333, 8.7, 0.5],

        ['yellow dal tadka', 149, 9, 6],

        ['veg kofta', 143.7, 13.4, 19.7],

        ['urad chilka dal', 350, 23, 1.4],

        ['veg jalfrezi', 86, 1, 4],

        ['mattar paneer', 121.5, 6.3, 9.1],

        ['cabbage matar', 25, 1, 2.8],

        ['dal bukhara', 121, 5, 5.3],

        ['mattar kulcha', 450, 19, 10],

        ['kadai soya', 340, 11, 3],

        ['gobi adraki', 30, 2.2, 3.5],

        ['bagare baigan', 138.8, 2.4, 7.8],

        ['sarson ka saag', 239, 1.3, 8],

        ['veg korma dal', 133.9, 2.8, 4.4],

        ['methi dal', 175, 6, 2],

        ['aloo palak', 93, 2.8, 3.8],

        ['gatta curry', 110, 5.4, 16],

        ['paneer butter masala', 211, 9.2, 16.6],

        ['nutri keema', 155, 52, 7.9],

        ['curry', 103.3, 9, 15],

        ['curry lobiya masala', 115, 8, 3.2],

        ['kadhai veg paneer', 189, 5.5, 12.8],

        ['malai kofta', 217, 6, 9.5],

        ['aloo pyaz', 98, 2.4, 6]
    ]
    return l


def breakfast_less():
    l = [
        ['tomato ketchup', 112, 1.3, 0.2],

        ['tea', 17, 0.5, 0.4],

        ['coconut chutney', 163, 3.58, 33.2],

        ['jam', 278, 0.4, 0.1],

        ['milk', 42, 3.4, 1],

        ['coffee', 17, 0.12, 0.02],

        ['cornflakes', 357, 8, 0.4],

        ['chocos', 387, 19, 3]
    ]
    return l


def lunch_less():
    l = [
        ['hot garlic sauce', 176.4, 5.2, 33.8],

        ['onion', 44.3, 1.1, 0.1],

        ['sirka onion', 42, 1.2, 8.8],

        ['kimchi salad', 97.4, 1.7, 7.9],

        ['green salad', 23.2, 1.5, 0.24],

        ['moong sprouts', 30, 3.4, 0.3]
    ]
    return l


def snacks_less():
    l = [
        ['tomato ketchup', 112, 1.3, 0.2],

        ['tea', 17, 0.5, 0.4],

        ['green chutney', 14, 5, 8.2],
        ['nimbu pani', 40, 0.1, 0.3],

        ['sweet chutney', 149, 0.6, 0.2],

        ['coffee', 17, 0.12, 0.02]
    ]
    return l


def dinner_less():
    l = [
        ['laccha onion', 44, 2, 4],

        ['hot n sour soup', 39, 2.6, 1.2],

        ['cucumber', 15, 2, 0.1],

        ['fruit custard', 83.3, 6.5, 7.7],

        ['manchow soup', 420, 7, 4.2],

        ['sweet corn soup', 49, 1.6, 0.3],

        ['custard', 122, 4, 4],

        ['sewaiyan kheer', 244.3, 10, 12],

        ['onion', 44.3, 1.1, 0.1],

        ['atta halwa', 186, 2.8, 6.5],

        ['shahi tukda', 396, 7, 17],

        ['cream of spinach soup', 80.6, 3, 4.8],

        ['mooli cream of spinach', 74, 3.5, 5],

        ['veg clear soup', 32, 1.7, 1.9],

        ['tamatar dhaniya ka shorba', 94, 11.5, 12.5],

        ['mooli', 16, 0.7, 0.1],

        ['cream of cauliflower soup', 52, 3, 4.7],

        ['tomato basil soup', 44, 1, 1.4],

        ['besan ladoo', 500, 10, 24.6],

        ['besan burfi', 648, 13.1, 4.5],

        ['vermicelli kheer', 244.13, 3.06, 1.9]
    ]
    return l
