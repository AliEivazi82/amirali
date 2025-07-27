from random import choice

soalha = ["fav food?", "fav color?", "how old is he/she?"]

person = {"Fname":"Akbar", "Lname":"Talebi", "fav food":"ghorme sabzi", "fav color": "pink", "age":64}

while True:
    soal = choice(soalha)
    javab = input(soal)


    if javab == "end":
        break

    if soal == "fav food?":

        if javab == person["fav food"]:
            print("doroste✅")
        else:
            print("Eshtebah❌")

        
