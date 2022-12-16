class car:
    wheels=4
    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil
    
car1=car("Merc","9")
car2=car("Thar","5")
car.wheels=6
print(car1.brand,car1.mil,car1.wheels)
print(car2.brand,car2.mil,car1.wheels)
