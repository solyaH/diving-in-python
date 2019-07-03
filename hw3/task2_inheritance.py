import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'Car'
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'Truck'
        self.set_whl(body_whl)

    def set_whl(self, body_whl):
        if body_whl == '':
            temp_list = [0] * 3
        else:
            temp_list = [float(i) for i in body_whl.split('x')]
        self.body_width = temp_list[0]
        self.body_height = temp_list[1]
        self.body_length = temp_list[2]

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'SpecMachine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], float(row[5]), row[2]))
                elif row[0] == 'truck':
                    car_list.append(
                        Truck(row[1], row[3], float(row[5]), row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(
                        SpecMachine(row[1], row[3], float(row[5]), row[6]))
            except ValueError:
                print('incorrect input')
            except IndexError:
                print('list index out of range')

    return car_list


if __name__ == '__main__':
    for item in get_car_list('../../cars.csv'):
        print(item.get_photo_file_ext())
        if isinstance(item, Truck):
            print(item.get_body_volume())
