import json

class Car():
    brand = ""
    color = ""
    model = 0
    name_user = ""

    def __init__(self,brand = "", color = "", model = 0, name_user = "") -> None:
        self.brand = brand
        self.color = color
        self.model = model
        self.name_user = name_user

    
    def __str__(self):
        car_dict = {
            "Brand": self.brand,
            "Color": self.color,
            "Model": self.model,
            "Name_user": self.name_user 
        }
        return json.dumps(car_dict, indent=4)
    
      # staticmethod
    def from_dict(car_dict):
        return Car(
            brand=car_dict.get("Brand", ""),
            color=car_dict.get("Color", ""),
            model=car_dict.get("Model", 0),
            name_user=car_dict.get("Name_user", "")
        )