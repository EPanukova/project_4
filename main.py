class Carbase:
    """Class Carbase"""
    def __init__(self, car_type = None, brand = None, photo_le_name = None):
        """Initialization method"""
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name


class Car(Carbase):
    """Class Car"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl = None, carrying = None):
        """Initialization method"""
        super().__init__(car_type, brand, photo_le_name)
        self.carrying = float(carrying) or None
        self.passenger_seats_count = int(passenger_seats_count) or None


class Truck(Carbase):
    """Class Truck"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None):
        """Initialization method"""
        super().__init__(car_type, brand, photo_le_name)
        self.carrying = float(carrying)
        self.body_whl = body_whl

        if self.body_whl is not None:
            self.body_whl = body_whl.split('x')
            if len(self.body_whl) <= 2 or self.body_whl[0] == '':
                self.body_width = 0
                self.body_height = 0
                self.body_length = 0
            else:
                self.body_width = float(self.body_whl[0])
                self.body_height = float(self.body_whl[1])
                self.body_length = float(self.body_whl[-1])
        else:
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
        self.body_whl = body_whl
        self.carrying = float(carrying)
        self.extra = extra


def get_car_list(filename):
    """Method get cars"""
    car_list = []
    with open(filename, encoding='utf-8') as file_cars:
        all_info = file_cars.readlines()
        for i in all_info:
            i = i.split(';')[:-1]
            try:
                if i[0] == 'car':
                    car_list.append(Car(*i))
            except TypeError:
                pass
            try:
                if i[0] == 'truck':
                    car_list.append(Truck(*i))
            except TypeError:
                pass
            try:
                if i[0] == 'spec_machine':
                    car_list.append(Specmachine(*i))
            except TypeError:
                pass
    return car_list


def main():
    """Main function"""
    get_car_list('solution.txt')

if __name__ == '__main__':
    main()
