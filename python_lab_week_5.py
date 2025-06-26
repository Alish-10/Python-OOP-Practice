# Python OOP Practice - Week 5: Inheritance and Polymorphism
#Exercise 1: Create a base class Vehicle and a derived class Car. Implement polymorphism in the move method.
# class Vehicle:
#     def __init__(self, colour, weight, max_speed, max_range=None):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.max_range = max_range

#     def move(self, speed): 
#         print(f"The vehicle is moving at {speed} km/h")
        
        
# class Car(Vehicle):
#     def __init__(self, colour, weight, max_speed,form_factor, max_range=None):
#         self.form_factor = form_factor
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.max_range = max_range
        
#     def move(self, speed):
#         print(f"The car is driving at {speed} km/h")

# # Create objects and test them OUTSIDE the class definitions
# generic_vehicle = Vehicle("red", 1000, 200)
# generic_vehicle.move(100)

# car = Car("blue", 1200, 220, "SUV")
# car.move(150)

# #Exercise 2: Using Super() in the Car class to call the base class constructor.
# class Electric(Car):
#     def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, max_range=None):
#         super().__init__(colour, weight, max_speed, form_factor, max_range)
#         self.battery_capacity = battery_capacity

#     def move(self, speed):
#         print(f"The electric car is driving silently at {speed} km/h  and has a maximum range of {self.max_range} km")

# class Petrol(Car):
#     def __init__(self, colour, weight, max_speed, form_factor, fuel_type, max_range=None):
#         super().__init__(colour, weight, max_speed, form_factor, max_range)
#         self.fuel_type = fuel_type

#     def move(self, speed):
#         print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km")
        
# electric_car = Electric("green", 1300, 180, "Sedan", 75 ,100)
# electric_car.move(120)

# petrol_car = Petrol("black", 1500, 240, "Coupe", "Petrol",150)
# petrol_car.move(200)

# generic_vehicle = Vehicle("white", 1100, 190)
# generic_vehicle.move(80)

#Exercise 3: kwargs parameter in the Vehicle class constructor
#  Task Modify the Electric and Petrol classes to include **kwargs in the __init__ method and
# susequently pass the keyword arguments to the Vehicle class via the super() function

# class Vehicle:
#     def __init__(self, colour, weight, max_speed):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed

#     def move(self, speed):
#         print(f"The vehicle is moving at {speed} km/h")
        
# class Car(Vehicle):
#     def __init__(self, colour, weight, max_speed,form_factor, max_range=None):
#         self.form_factor = form_factor
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.max_range = max_range

# class Electric(Car):
#     def __init__(self, max_range, **kwargs):
#         super().__init__(**kwargs)
#         self.max_range = max_range

#     def move(self, speed):
#         print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")

# class Petrol(Car):
#     def __init__(self, max_range, **kwargs):
#         super().__init__(**kwargs)
#         self.max_range = max_range

#     def move(self, speed):
#         print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km")

# Test the classes
# electric_car = ElectricCar(max_range=100, colour="green", weight=1500, max_speed=180)
# petrol_car = PetrolCar(max_range=600, colour="black", weight=1400, max_speed=200)

# electric_car.move(100)
# petrol_car.move(120)

#Task: Adding more classes for Plane, Propeller, and Jet

# class Plane(Vehicle):
#     def __init__(self, wingspan, **kwargs):
#         super().__init__(**kwargs)
#         self.wingspan = wingspan

#     def move(self, speed):
#         print(f"The plane is flying at {speed} km/h with a wingspan of {self.wingspan} meters")

# class Propeller(Plane):
#     def __init__(self, propeller_diameter, **kwargs):
#         super().__init__(**kwargs)
#         self.propeller_diameter = propeller_diameter

#     def move(self, speed):
#         print(f"The propeller plane is flying at {speed} km/h with a wingspan of {self.wingspan} meters and a propeller diameter of {self.propeller_diameter} meters")

# class Jet(Plane):
#     def __init__(self, engine_thrust, **kwargs):
#         super().__init__(**kwargs)
#         self.engine_thrust = engine_thrust

#     def move(self, speed):
#         print(f"The jet is flying at {speed} km/h with a wingspan of {self.wingspan} meters and an engine thrust of {self.engine_thrust} kN")

# Test the classes
# electric_car = Electric(max_range=100, colour="green",form_factor = "sedan", weight=1500, max_speed=180)
# petrol_car = Petrol(max_range=600, colour="black", weight=1400, form_factor = "ev", max_speed=200)
# propeller_plane = Propeller(propeller_diameter=3.5, wingspan=15, colour="white", weight=1200, max_speed=350)
# jet_plane = Jet(engine_thrust=120, wingspan=25, colour="silver", weight=8000, max_speed=900)

# electric_car.move(100)
# petrol_car.move(120)
# propeller_plane.move(250)
# jet_plane.move(800)

#Exercise 4: Multiple inheritance
class Vehicle:
    def __init__(self, colour, weight, max_speed, **kwargs):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        for key, value in kwargs.items():
            setattr(self, key, value)

class Plane(Vehicle):
    def __init__(self, wingspan, **kwargs):
        self.wingspan = wingspan
        super().__init__(**kwargs)

class Car(Vehicle):
    def __init__(self, form_factor, **kwargs):
        self.form_factor = form_factor
        super().__init__(**kwargs)

class FlyingCar(Car, Plane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def move(self, speed):
        print(f"The flying car is driving or flying at {speed} km/h")

# Usage:
generic_flying_car = FlyingCar(colour="red", weight=1000, max_speed=200, form_factor="SUV", wingspan=30, seats=5)
generic_flying_car.move(100)
print(generic_flying_car.seats, generic_flying_car.wingspan, generic_flying_car.form_factor)
        
generic_flying_car_2 = FlyingCar(colour="red", weight=1000, max_speed=200, 
form_factor="SUV", wingspan=30, seats=5) 
generic_flying_car_2.move(100)

# Polymorphism in action
class Animal: 
# we omit the __init__ method for brevity 
    def move(self, speed): 
        print(f"The animal is moving at a speed of {speed}") 
generic_animal = Animal() 
generic_animal.move(20)

for movable_object in [ generic_flying_car, generic_flying_car_2,
generic_animal]: 
    movable_object.move(20) 