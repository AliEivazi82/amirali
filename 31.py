# with open(r".\hello\foods.txt", "w") as file: # write --> نوشتن
#     text = "pizza"
#     file.write(text)
#     file.close()

with open(r".\hello\foods.txt", "a") as file: # append
    text = "pasta"
    file.write(f"{text}\n")
    file.close()
