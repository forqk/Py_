import os.path
import csv


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ex(cls):
        fullpath = os.path.splitext(cls.photo_file_name)
        print(fullpath[1])


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_length, self.body_width, self.body_height = 0, 0, 0
        self.__parseWhl(body_whl)

    def __parseWhl(self, body_whl):
        whl = body_whl.split('x')
        for number in whl:
            if not isfloat(number) and len(whl) != 3:
                return
        self.body_length = whl[0]
        self.body_width = whl[1]
        self.body_height = whl[2]


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)

        self.car_type = "spec_machine"
        self.extra = extra


def CheckCommonAttribute(row):
    possible_technics = ['car', 'truck', 'spec_machine']
    possibe_img_extansions = ['.png', '.jpg', '.jpeg', '.gif']
    if len(row) != 7 \
        or row["car_type"] not in possible_technics \
        or not isinstance(row["brand"], str) \
        or not (isfloat(row["carrying"]) or isInt(row["carrying"])) \
        or not isinstance(row["photo_file_name"], str) \
        or os.path.splitext(row["photo_file_name"])[1] not in possibe_img_extansions:
        return False
    return True

def ParseCar(row):
    requared_attributes = ["car_type", "photo_file_name", "brand", "carrying", "passender_seats_count"]
    usless_attributes = ["body_whl", "extra"]
    
    
    
def ParseFile(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
       # next(reader)  # пропускаем заголовок
        for row in reader:
            if CheckCommonAttribute(row) == False:
                continue
                
            if row["car_type"] == 'car':
                car = ParseCar(row);

            print(row)


def get_car_list(csv_filename):
    car_list = []
    return car_list


def main():
    # car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    # print(car.car_type, car.brand, car.photo_file_name,
    #       car.carrying, car.passenger_seats_count, sep='\n')
    # truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    # print(truck.car_type, truck.brand, truck.photo_file_name,
    #       truck.body_length, truck.body_width, truck.body_height, sep='\n')
    # spec_machine = SpecMachine(
    #     'Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    # print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,
    #       spec_machine.photo_file_name, spec_machine.extra, sep='\n')
    # print(spec_machine.get_photo_file_ex())
    ParseFile("cars_week3.csv")


main()
