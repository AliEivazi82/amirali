import random

def pizza(money:float):
    type_of = {
        20:"peperoni",
        35:"meat & mashroom",
        30:"greek",
        25:"garlic"
    }
    prices = list(type_of.keys())
    for price in prices:
        if price > money:
            print("it's bigger", price)
        elif price < money:
            print("it's smaller", price)
        else:
            print("mosavi", price)
    

pizza(22)
