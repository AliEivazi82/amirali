import os

os.system("cls")

print("salam be barname mashin hesab khosh omadid😀")


fname = input("esm shoma chist? (ya pass)")
if fname == "pass":
    pass
else:
    lname = input("family shoma chist? ")

os.system("cls")
q = input("soal riazi khodet ro bego?") # "5+7"

first_number , alamat , second_number = q.split()

if alamat == "+":
    print(int(first_number)+ int(second_number))
elif alamat == "-":
    print(int(first_number)- int(second_number))
elif alamat == "*":
    print(int(first_number)* int(second_number))
elif alamat == "/":
    print(int(first_number)/ int(second_number))
else:
    print("Error! Not Found")
