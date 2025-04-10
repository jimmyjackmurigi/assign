class Superhero:
    def __init__(self, name, alias, power):
        self.name = name
        self.alias = alias
        self.power = power
        self._base_location = "Unknown"

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}. My power is {self.power}.")

    def reveal_base(self):
        print(f"{self.alias}'s base is at: {self._base_location}")


class Batman(Superhero):
    def __init__(self, gadgets):
        super().__init__("Bruce Wayne", "Batman", "Intelligence & Martial Arts")
        self.gadgets = gadgets
        self._base_location = "Batcave"

    def introduce(self):
        print(f"🦇 I am Batman! I fight crime using gadgets like {', '.join(self.gadgets)}.")


batman = Batman(["Batarang", "Grapple Gun", "Batmobile"])
batman.introduce()
batman.reveal_base()


class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")




vehicles = [Car()]

for vehicle in vehicles:
    vehicle.move()
