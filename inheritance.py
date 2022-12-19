class vehicle:
    def category(self):
        print("i am vehicle")
    def seatingCapacity(self):
        print("Seating capacity:4")
class bus(vehicle):
    def seatingCapacity(self):
        print("Seating capacity:30")
class thar(vehicle):
    pass
class wrangler(vehicle):
    pass
   
objvehicle=vehicle()
objbus=bus()
objthar=thar()
objwrangler=wrangler()

objbus.category()
objbus.seatingCapacity()
objthar.category()
objthar.seatingCapacity()
objwrangler.category()
objwrangler.seatingCapacity()
