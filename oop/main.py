from oop.vehicles import Bicycle, Car, Motorcycle

bicycle = Bicycle('Peugeot')
car1 = Car('Chevrlet Corvette', 4500, 'petrol', 2, 2)
car2 = Car('Volkswagen Passat', 2000, 'diesel', 5, 4)
motorcycle = Motorcycle('Harley Davidson', 2200, 'petrol')

try:
    bicycle.move(2)
except AttributeError:
    print('Bicycles do not have "move" method')
try:
    car1.move(2)
    car2.move(2)
except AttributeError:
    print('Cars do not have "move" method')
try:
    motorcycle.move(2)
except AttributeError:
    print('Motorcycles do not have "move" method')
try:
    bicycle.tank(10)
except AttributeError:
    print('Bike  do not have "tank" method')
try:
    car1.tank(10)
    car2.tank(10)
except AttributeError:
    print('Cars  do not have "tank" method')
try:
    motorcycle.tank(10)
except AttributeError:
    print('Motorcycles  do not have "tank" method')
try:
    bicycle.carry()
except AttributeError:
    print('Bike  do not have "carry" method')
try:
    motorcycle.carry()
except AttributeError:
    print('Motorcycle  do not have "carry" method')
try:
    car1.carry()
    car2.carry()
except AttributeError:
    print('Cars  do not have "carry" method')
