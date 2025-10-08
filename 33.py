import json

path = r".\data\cars.json"

with open(path, "r") as file:
    cars_data = json.load(file)
    file.close()

with open(path, "w") as file:
    new_data = {
        "name of car": "kmc t8",
        "year": 2024,
        "origin color": "black",
        "number of wheels": 4,
        "number of doors": 4,
        "price": 70000.00
    }
    cars_data.append(new_data)
    file.write(json.dumps(cars_data, indent=4))
