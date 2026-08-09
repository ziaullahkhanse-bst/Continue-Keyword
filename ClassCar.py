class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting!")

    def info(self):
        return f"{self.brand} {self.model} ({self.year})"

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.start()
print(car1.info())

car2.start()
print(car2.info())