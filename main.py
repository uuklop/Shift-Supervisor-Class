import employee

# creating the main method
def main():

  # Getting the user input
    print('\nEmployee Data')
    emp_name = input("Employee name: ")
    emp_number  = input("Employee number: ")

    # Creating the object for employee class
    employee_one = employee.Employee(emp_name, emp_number)

    # creating the object for the shift supervisor
    print('\nProduction worker details')
    emp_name = input("Employee name: ")
    emp_number  = input("Employee number: ")
    annual_salary = float(input('Annual Salary: '))
    annual_bonus = float(input('Annual Bonus: '))
     
    #  Creating the object for production worker class
    shift_supervisor = employee.ShiftSupervisor(emp_name, emp_number, annual_salary, annual_bonus)

    # Displaying the results
    print(f'\nEmployee Data')
    print(f'---------------')
    print(f'Employee Name: {employee_one.return_emp_name()}')
    print(f'Employee Number: {employee_one.return_emp_number()}') 


    print('\nSalary and Bonus Details')
    print('--------------------------')
    print(f'Employee Name: {shift_supervisor.return_emp_name()}')
    print(f'Employee Number: {shift_supervisor.return_emp_number()}') 
    print(f'Annual Salary: {shift_supervisor.get_annual_salary()}')
    print(f'Annual Production Bonus: {shift_supervisor.get_annual_production()}')

# Calling the main function
main()