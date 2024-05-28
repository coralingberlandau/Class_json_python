import json
import os
from helper.car import Car

def load_data_from_json(filename, cars):
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)  
            return []
        with open(filename, 'r') as file:
            car_data = json.load(file)
            return [Car.from_dict(car) for car in car_data]
    except FileNotFoundError:
        print(f'File {filename} not found.')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from file {filename}.')

def save_data_to_json(file_path, cars):
    try:
        with open(file_path, 'w') as file:
            car_data = [json.loads(str(car)) for car in cars]
            json.dump(car_data, file, indent=4)
            print(f'Data saved to {file_path}')
    except Exception as e:
        print(f'Error saving data to {file_path}:', e)

def reset_data_from_json(file_path, cars):
    cars = []
    print('Car data restarted and reloaded from file.')
    save_data_to_json(file_path, cars)