# Creating the employee class

class Employee:

    # setting up the empoyee constructor
    def __init__(self, emp_name, emp_number):
        self.__emp_name = emp_name
        self.__emp_number = emp_number

    # defining the accessors and mutators for the attributes
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
    
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def return_emp_name(self):
        return self.__emp_name
    
    def return_emp_number(self, ):
        return self.__emp_number 


# Creating the shift supervisor class

class ShiftSupervisor(Employee):
    
    # setting up the constructor
    def __init__(self, emp_name, emp_number, annual_salary, ann_prod_bonus):
        Employee.__init__(self, emp_name, emp_number)
        self.__ann_salary = annual_salary
        self.__ann_production = ann_prod_bonus

    def set_annual_salary(self, annual_salary):
        self.__ann_salary = annual_salary

    def set_ann_production(self, annual_production_salary):
        self.__ann_production = annual_production_salary

    def get_annual_salary(self):
        return self.__ann_salary

    def get_annual_production(self):
        return self.__ann_production
