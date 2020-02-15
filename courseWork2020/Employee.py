from Person import *
class Employee(Person):

  def __init__(self,name,age,employee_department,employee_salary):
    super(Employee, self).__init__(name,age)
    self.employee_department = employee_department
    self.employee_salary=employee_salary
    self.employee_email="n/a"

  def set_employee_email(self,email):
    self.employee_email = email


  def get_employee_salary(self):
    return self.employee_salary

  def get_employee_info(self):
   return 'Name - {name}; age - {age}; salary - {salary}; email - {email}'.format(name=self.name,age=self.age,department=self.employee_department
   ,salary=self.employee_salary
   ,email=self.employee_email)
