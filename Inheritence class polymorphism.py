class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class car(vehicle):
    def move(self):
        print("move")

class boat(vehicle):
    def move(self):
        print("sail")

class plane(vehicle):
    def move(self):
        print("Fly")

car1=car("ford","mustang")
boat1=boat("titanic","touring")
plane1=plane("Boeing",747)

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
