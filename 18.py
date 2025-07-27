import time
import os

x = 0
while True:
    print(x)
    x += 1
    time.sleep(0.3)
    os.system("cls")

    if x == 50:
        break

print("salam")

# while True:
#     print("amirali")
#     continue
#     print("Ali")