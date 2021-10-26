from Fruit import Fruit
from Animal import Animal
from Customer import ReturningCustomer
from Employee import PartTimeEmployee
from Triangle import Triangle
from Car import ElectricCar

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

class Square(object):
  def __init__(self):
    self.sides = 4
 
my_shape = Square()
print (my_shape.sides)

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

zebra.description()
giraffe.description()
panda.description()

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

milton = PartTimeEmployee('Milton')
print (milton.calculate_wage(20))
print (milton.full_time_wage(40))

my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print(my_car.display_car())


