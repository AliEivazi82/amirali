
path = r".\projects\contacts.txt"

while True:
    print("1)Add\n2)Read\n3)End\n4)delete")
    user = input("Entekhab kon: ")

    if user.lower().strip() == "end" or user.strip() == "3": #* END
        print("ok, Googbye🙌")
        break

    elif user == "add": #* ADD
        with open(path, "a") as file:
            username = input("Enter The Name: ")
            number = input("Enter The Number: ")
            file.write(f"username: {username} | number: {number}\n")
            file.close()

    elif user == "read": #* READ
        with open(path, "r") as file:
            print(file.read(), end="\n\n+=+=+=+=+=+=+=+=\n")

    elif user == "delete":
        with open(path, 'r') as file:
            lines = file.read().split('\n')
            del_username = input("who do you want to delete: ")
            for line in lines:
                if line.startswith(f"username: {del_username}"):
                    lines.remove(line)
                    print(lines)
                else:
                    print("this username not found | 404")
            file.close()
        
        with open(path, 'w') as file:
            for line in lines:
                file.write(f"{line}\n")
            file.close()

    else:
        print("lotfan yki az gozine ha ro entekhab kon!!!")
