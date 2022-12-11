class person:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def printo(self):
        print("Name is:",self.name,"and his roll number is:",self.roll_no)
        print(id(person1))
        print(id(person2))

person1=person("Gurnoor","12")
person2=person("Ankur","25")

person1.printo()
person2.printo()