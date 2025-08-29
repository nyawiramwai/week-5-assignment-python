class Vehicle:
    def move(self):
        pass  
class Car(Vehicle):
    def move(self):
        print(" Driving on the road!")
class Plane(Vehicle):
    def move(self):
        print(" Flying in the sky!")
class Boat(Vehicle):
    def move(self):
        print(" Sailing on the water!")
class Train(Vehicle):
    def move(self):
        print(" Running on the tracks!")