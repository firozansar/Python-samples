class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00


class PartTimeEmployee(Employee):
 # calculate_wage below override calculate_wage of parent class!
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

