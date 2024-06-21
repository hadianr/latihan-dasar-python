class Vehicle:
  """
  This class represents a generic vehicle.
  """
  def __init__(self, max_speed):
    self.max_speed = max_speed

  def accelerate(self):
    print(f"The vehicle is accelerating up to {self.max_speed} km/h.")

class Car(Vehicle):
  """
  This class represents a car, inheriting from the Vehicle class.
  """
  def __init__(self, max_speed, num_doors):
    # Call the parent class constructor (Vehicle) to initialize max_speed
    super().__init__(max_speed)  
    self.num_doors = num_doors

  def drive(self):
    print(f"Driving the car with {self.num_doors} doors.")

class Bicycle(Vehicle):
  """
  This class represents a bicycle, inheriting from the Vehicle class.
  """
  def __init__(self, max_speed, has_gears):
    # Call the parent class constructor (Vehicle) to initialize max_speed
    super().__init__(max_speed)  
    self.has_gears = has_gears

  def pedal(self):
    print(f"Pedaling the bicycle with gears: {self.has_gears}.")

# Create objects
car = Car(180, 4)
bicycle = Bicycle(30, True)

# Use methods
car.accelerate()  # Inherited from Vehicle
car.drive()

bicycle.accelerate()  # Inherited from Vehicle
bicycle.pedal()

print("Car max speed:", car.max_speed)  # Access inherited attribute