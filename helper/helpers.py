from helper.car import Car
from helper.json import save_data_to_json

def add_car(cars):
    temp_car = Car(input("Brand:"), input("Color:"), input("Model:"), input("Name_user:"))
    cars.append(temp_car)
    save_data_to_json('cars.json', cars)

def print_car_data(cars):
    for index, car in enumerate(cars):
        print(index, car)

def delete_car(cars):
    car_index_select = car_index(cars)
    cars.pop(car_index_select)
    save_data_to_json('cars.json', cars)

def car_index(cars):
    print_car_data(cars)
    car_index_select = int(input("Select the index of the car you want: "))
    return car_index_select

def update_car(cars):
    car_index_select = car_index(cars)
    cars[car_index_select] =Car(input("Brand:"), input("Color:"), input("Model:"), input("Name_user:"))
    save_data_to_json('cars.json', cars)

def sum_cars(cars):
    total_cars = len(cars)
    print(f'Do you have {total_cars} cars')