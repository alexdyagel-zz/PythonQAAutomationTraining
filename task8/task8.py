class Car(object):
    DEFAULT_WHEELS_NUMBER = 5
    DEFAULT_WHEELS_NUMBER_FOR_RED_CARS = 4
    DEFAULT_COLOR = "black"
    count = 0

    def __init__(self, model, color=DEFAULT_COLOR, wheels=DEFAULT_WHEELS_NUMBER):
        if wheels < 0:
            raise ValueError("Number of wheels cant be less than 0")

        self.model = model
        self.color = color
        if self.color == "red":
            wheels = self.DEFAULT_WHEELS_NUMBER_FOR_RED_CARS
        self.wheels = wheels
        Car.count += 1

    def diag(self):
        print("model: {}".format(self.model))
        print("color: {}".format(self.color))
        print("wheels number: {}".format(self.wheels))

    @staticmethod
    def print_number_of_created_cars():
        print("number of created cars: {}".format(Car.count))


mazda = Car("mazda", "red", 10)
audi = Car("audi", "blue")
bmw = Car("bmw x5")
mazda.diag()
audi.diag()
bmw.diag()
Car.print_number_of_created_cars()
