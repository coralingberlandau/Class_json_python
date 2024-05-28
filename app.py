"""
This application manage a garage.  
"""
from enum import Enum
from helper.helpers import add_car, delete_car, print_car_data, sum_cars, update_car, car_index
from helper.json import load_data_from_json, restart_data_from_json, save_data_to_json

cars = []

class Menu(Enum):
    ADD = 1
    PRINT = 2
    DELETE = 3
    UPDATE = 4
    SUM = 5
    RESTART = 6
    EXIT = 7
    
def display_menu():
    for men in Menu:
        print(f'{men.value} - {men.name}')
    return Menu(int(input("Enter what you want:")))

if __name__ == '__main__':
    cars = load_data_from_json('cars.json', cars)
    print(f'{len(cars)} cars loaded from cars.json')
    while True:
        try:
            user_select = display_menu()
            if user_select == Menu.ADD: add_car(cars)
            if user_select == Menu.PRINT: print_car_data(cars)
            if user_select == Menu.DELETE: delete_car(cars)
            if user_select == Menu.UPDATE: update_car(cars)
            if user_select == Menu.SUM: sum_cars(cars)
            if user_select == Menu.RESTART: 
                restart_data_from_json('cars.json', cars)
                cars = load_data_from_json('cars.json', cars)
            if user_select == Menu.EXIT:
                save_data_to_json('cars.json', cars)
                exit()
        except Exception as e:
            print("Error:", e)