from Employee import *


class Department(Employee):
    def __init__(self, department_name):
        self.department_name = department_name
        self.employes = []

    def add_employes(self, Employee):
        self.employes.append(Employee)


    def calculate_avg_salary_of_department(self):
        sum = 0.0
        for i in self.employes:
            sum = sum + i.get_employee_salary()
        return sum / len(self.employes)

    def get_employee_salary(self):
        return super().get_employee_salary()


    def print_info(self):
        self.employes.sort(key=lambda x: x.get_employee_salary(),reverse=True)
        print(self.department_name+":      Average salary=",self.calculate_avg_salary_of_department())
        for Employee in self.employes:
            print(Employee.get_employee_info())
