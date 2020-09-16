class Carbase:
    """Class Carbase"""
    def __init__(self, car_type = None, brand = None, photo_le_name = None):
        """Initialization method"""
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name


class Car(Carbase):
    """Class Car"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_width = None, carrying = None):
        """Initialization method"""
        super().__init__(car_type, brand, photo_le_name)
        self.carrying = carrying
        self.passenger_seats_count = int(passenger_seats_count) or None
        self.body_width = body_width


class Truck(Carbase):
    """Class Truck"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl = None, carrying=None):
        """Initialization method"""
        super().__init__(car_type, brand, photo_le_name)
        self.passenger_seats_count = None
        self.carrying = carrying
        self.body_whl = self.body_whl

        if self.body_whl is not None:
            self.body_whl = str(body_whl).split('x')
            self.body_width = float(self.body_whl[0])
            self.body_height = float(self.body_whl[1])
            self.body_length = float(self.body_whl[-1])
        else:
            self.body_whl = None
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0

    def get_body_volume(self):
        """Engine volume calculation method"""
        if self.body_whl is not None:
            engine_volume = float(self.body_width)*float(self.body_height)*float(self.body_length)
        else:
            engine_volume = 0
        return float(engine_volume)


class Specmachine(Carbase):
    """Class Specmachine"""
    def __init__(self ,car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None, extra=None):
        """Initialization method"""
        super().__init__(car_type, brand, photo_le_name)
        self.passenger_seats_count = int(passenger_seats_count) or None
        self.body_whl = body_whl
        self.carrying = carrying
        self.extra = extra


def get_car_list(filename):
    """Method get cars"""
    car_list = []
    with open(filename) as file_cars:
        all_info = file_cars.readlines()
        for i in all_info:
            i = i.split(';')[:-1]
            if i[0] == 'car':
                car_list.append(Car(*i))
            if i[0] == 'truck':
                car_list.append(Truck(*i))
            if i[0] == 'spec_machine':
                car_list.append(Specmachine(*i))
    return car_list


def main():
    """Main function"""
    get_car_list('solution.txt')
    #print(Truck.get_body_volume())
if __name__ == '__main__':
    main()
