from Department import *
from Employee import *
if __name__ == '__main__':


    departments=[]

    department1 = Department("Development")
    department2 = Department("Marketing")



    emp1=Employee("Pesho",28,"Development",1200)
    emp1.set_employee_email("pesho@abv.bg")
    department1.add_employes(emp1)

    emp2=Employee("Toncho",33,"Marketing",1300)
    department2.add_employes(emp2)

    emp3 = Employee("Ivan",19,"Development",1000)
    emp3.set_employee_email("ivan@ivan.com")
    department1.add_employes(emp3)

    emp4 = Employee("Stanimir",22,"Marketing",1088)
    emp4.set_employee_email("stancho@yahoo.com")
    department2.add_employes(emp4)

    departments.append(department1)
    departments.append(department2)

    departments.sort(key=lambda x:x.calculate_avg_salary_of_department(),reverse=True)

    for Department in departments:
        Department.print_info()
