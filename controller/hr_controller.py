from sqlite3 import Date
from model.hr import hr
from view import terminal as view
from model import data_manager, util
from controller import main_controller
from datetime import date, datetime, timedelta


def list_employees():
    list_employees = hr.get_list_customers()
    headers = hr.HEADERS
    view.print_table_hr(list_employees)


def add_employee():
    list_employees = hr.get_list_customers()
    new_employee = view.get_inputs_hr()
    list_employees.append(new_employee)
    data_manager.write_table_to_file(hr.DATAFILE, list_employees, separator=';')

def get_employee_from_id(list_employees, employee_id_to_update):
    for item, sublist in enumerate(list_employees):
        try:
            return (item, sublist.index(employee_id_to_update))
        except ValueError:
            continue
    return None


def update_employee():
    list_employees = hr.get_list_customers()
    employee_id_to_update = input(
        "In order to update a customer, please enter an ID: ")
    employee_tuple = get_employee_from_id(list_employees, employee_id_to_update)
    employee_index = employee_tuple[0]
    if employee_tuple is not None:
        employee_update_name = str(input("Update name: "))
        employee_update_Date_of_birth = str(input("Update Date of birth: "))
        employee_update_Department = str(input("Update Department: "))
        employee_update_Clearance = str(input("Update Clearance: "))
        employee_update = [employee_id_to_update, employee_update_name, employee_update_Date_of_birth,  employee_update_Department,employee_update_Clearance ]
        list_employees[employee_index] = employee_update
        data_manager.write_table_to_file(hr.DATAFILE, list_employees, separator=';')
    else:
        print("Not an ID in the list of customers")


def delete_employee():
    list_employees = hr.get_list_customers()
    employee_id_to_delete = input(
        "In order to delete a customer, please enter an ID: ")
    employee_tuple = get_employee_from_id(list_employees, employee_id_to_delete)
    employee_index = employee_tuple[0]
    if employee_tuple is not None:
        list_employees.pop(employee_index)
        data_manager.write_table_to_file(hr.DATAFILE, list_employees, separator=';')
    else:
        print("Not an ID in the list of customers")


def get_oldest_and_youngest():
    list_employees = hr.get_list_customers()
    year_list = []
    for employee in range(len(list_employees)):
        year_list.append(list_employees[employee][2])
    oldest_emplyee = max(year_list)
    oldest_emplyee_tuple = get_oldest_client(list_employees, oldest_emplyee)
    youngest_employee = min(year_list)
    youngest_employee_tuple = get_youngest_client(list_employees, youngest_employee)
    view.print_message(((list_employees[oldest_emplyee_tuple[0]][1]),(list_employees[youngest_employee_tuple[0]][1])))

def get_oldest_client(list_employees, oldest_emplyee):
    for item, sublist in enumerate(list_employees):
        try:
            return (item, sublist.index(oldest_emplyee))
        except ValueError:
            continue
    return None

def get_youngest_client(list_employees, youngest_emplyee):
    for item, sublist in enumerate(list_employees):
        try:
            return (item, sublist.index(youngest_emplyee))
        except ValueError:
            continue
    return None

def get_average_age():
    list_employees = hr.get_list_customers()
    birth_date_list = []
    current_year = 2022
    employees_birth_years_list = []
    for employee in range(len(list_employees)):
        birth_date_list.append(list_employees[employee][2])
    for year in birth_date_list:
        employees_birth_years_list.append(int(year.split("-")[0]))
    average_year = int(sum(employees_birth_years_list) / len(employees_birth_years_list))
    average_age = current_year - average_year
    view.print_message(average_age)


def next_birthdays():
    today = date.today()
    two_weeks_from_today = today +timedelta(weeks=2)
    delta = date.today() - two_weeks_from_today
    print(delta)
    print(two_weeks_from_today)
    view.print_message(today)
    list_employees = hr.get_list_customers()
    birth_date_list = []
    converted = []
    for employee in range(len(list_employees)):
        birth_date_list.append(list_employees[employee][2])
    print(birth_date_list)
    pass





def count_employees_with_clearance():
    list_employees = hr.get_list_customers()
    employees_with_clearance_level = []
    for employee in range(len(list_employees)):
        if list_employees[employee][4] != 0 :
            employees_with_clearance_level.append(list_employees[employee][4])
    print("Number of employees who have at least the input clearance level is :" , len(employees_with_clearance_level))


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")



def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        main_controller.menu()
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
