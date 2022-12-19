# class players:
#     def __init__(self):
#         print("This is ronaldo")
# class coach(players):
#     def method2(self):
#         print("This is erik")
# class owners:
#     def method3(self):
#         print("We are owners")

# objA=players()
# objB=coach()
# objC=owners()
class rect:
    def calculateArea(self,length,breadth):
        return length*breadth

    def calculateArea(self,length):
        return length*length

rectangle=rect()
print(rectangle.calculateArea(2,3))
print(rectangle.calculateArea(2))


