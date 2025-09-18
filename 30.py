# file = open("text.txt", "r") #read = خواندن
# print(file.read())
# file.close()

with open(r".\hello\text.txt", "r") as file:
    color1 , color2 , color3 = file.read().split("\n")
    # text = text.split()
    print(color1)
    print(color2)
    print(color3)
    file.close()
