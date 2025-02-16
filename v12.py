class  Vehicule:
    def __init__(self, make, model, year, mileage):
        self.make = make 
        self.model = model
        self.year = year 
        self.mileage = mileage

    def drive(self, miles):
        return self.mileage + miles


    def get_info(self):
        return f"{self.make} {self.model} ({self.year}) with {self.mileage} miles"
    
car = Vehicule("Toyota", "Corolla", 2020, 50000)
print(car.get_info())