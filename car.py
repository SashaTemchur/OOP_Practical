color_input = str(input(" TownCar color:"))
speed_input = int(input(" TownCar speed:"))
name_input = str(input(" TownCar name:"))
go_stop_input = str(input(" TownCar Go or Stop:"))
turn_input = str(input(" TownCar Right or Left:"))

color_input1 = str(input(" SportCar color:"))
speed_input1 = int(input(" SportCar speed:"))
name_input1 = str(input(" SportCar name:"))
go_stop_input1 = str(input(" SportCar Go or Stop:"))
turn_input1 = str(input(" SportCar Right or Left:"))

color_input2 = str(input(" WorkCar color:"))
speed_input2 = int(input(" WorkCar speed:"))
name_input2 = str(input(" WorkCar name:"))
go_stop_input2 = str(input(" WorkCar Go or Stop:"))
turn_input2 = str(input(" WorkCar Right or Left:"))

color_input3 = str(input(" PoliceTownCar color:"))
speed_input3 = int(input(" PoliceTownCar speed:"))
name_input3 = str(input(" PoliceTownCar name:"))
go_stop_input3 = str(input(" PoliceTownCar Go or Stop:"))
turn_input3 = str(input(" PoliceTownCar Right or Left:"))


class AllCars:
    # Creates a master class that makes master data for all others
    def __init__(self, speed, color, name, is_police, go_stop, right_left):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go_stop = go_stop
        self.turn = right_left


class TownCar(AllCars):
    # Creates a class TownCar that inherits the main class AllCars in this class displays the data you specified for the car
    def __init__(self, speed, color, name, is_police, go_stop, right_left):
        AllCars.__init__(self, speed, color, name,
                         is_police, go_stop, right_left)

    def get_decribed_name(self):
        long_color = str(self.color)
        long_name = str(self.name)
        long_speed = int(self.speed)
        long_police = bool(self.is_police)
        long_go_stop = str(self.go_stop)
        long_turn = str(self.turn)
        return " TownCar Speed: {}\n TownCar Color: {}\n TownCar Name: {}\n TownCar Is_police: {}\n TownCar Go or Stop: {}\n TownCar Turn Right or Left: {} \n\n\n".format(
            long_speed, long_color, long_name, long_police, long_go_stop, long_turn)


class SportCar(AllCars):
    # Creates a class SportCar that inherits the main class AllCars in this class displays the data you specified for the car
    def __init__(self, speed, color, name, is_police, go_stop, right_left):
        AllCars.__init__(self, speed, color, name,
                         is_police, go_stop, right_left)

    def get_decribed_name(self):
        long_color = str(self.color)
        long_name = str(self.name)
        long_speed = int(self.speed)
        long_police = bool(self.is_police)
        long_go_stop = str(self.go_stop)
        long_turn = str(self.turn)
        return "SportCar Speed: {}\n SportCar Color: {}\n SportCar Name: {}\n SportCar Is_police: {}\n SportCar Go or Stop: {}\n SportCar Turn Right or Left: {} \n\n\n".format(
            long_speed, long_color, long_name, long_police, long_go_stop, long_turn)


class WorkCar(AllCars):
    # Creates a class WorkCar that inherits the main class AllCars in this class displays the data you specified for the car
    def __init__(self, speed, color, name, is_police, go_stop, right_left):
        AllCars.__init__(self, speed, color, name,
                         is_police, go_stop, right_left)

    def get_decribed_name(self):
        long_color = str(self.color)
        long_name = str(self.name)
        long_speed = int(self.speed)
        long_police = bool(self.is_police)
        long_go_stop = str(self.go_stop)
        long_turn = str(self.turn)
        return "WorkCar Speed: {}\n WorkCar Color: {}\n WorkCar Name: {}\n WorkCar Is_police: {}\n WorkCar Go or Stop: {}\n WorkCar Turn Right or Left: {} \n\n\n".format(
            long_speed, long_color, long_name, long_police, long_go_stop, long_turn)


class PoliceCar(AllCars):
    # Creates a class PoliceCar that inherits the main class AllCars in this class displays the data you specified for the car
    def __init__(self, speed, color, name, is_police, go_stop, right_left):
        AllCars.__init__(self, speed, color, name,
                         is_police, go_stop, right_left)

    def get_decribed_name(self):
        long_color = str(self.color)
        long_name = str(self.name)
        long_speed = int(self.speed)
        long_police = bool(self.is_police)
        long_go_stop = str(self.go_stop)
        long_turn = str(self.turn)
        return "PoliceCar Speed: {}\n PoliceCar Color: {}\n PoliceCar Name: {}\n PoliceCar Is_police: {}\n PoliceCar Go or Stop: {}\n PoliceCar Turn Right or Left: {}".format(
            long_speed, long_color, long_name, long_police, long_go_stop, long_turn)


cars = TownCar(speed_input, color_input, name_input,
               False, go_stop_input, turn_input) # Specifies data for the machine
cars1 = SportCar(speed_input1, color_input1, name_input1,
                 False, go_stop_input1, turn_input1) # Specifies data for the machine
cars2 = WorkCar(speed_input2, color_input2, name_input2,
                False, go_stop_input2, turn_input2) # Specifies data for the machine
cars3 = PoliceCar(speed_input3, color_input3, name_input3,
                  True, go_stop_input3, turn_input3) # Specifies data for the machine
print(cars.get_decribed_name(), cars1.get_decribed_name(),
      cars2.get_decribed_name(), cars3.get_decribed_name())
