import random
import mysql.connector as sqlcon

# from xlwt import Workbook

all_employees = []
all_days = []
all_shifts = []
excluded_names_from_regular_shifts = []
excluded_employees_from_regular_shifts = []





class Employee:

    def __init__(self, idemployee, first_name, last_name, contract_shift_amount, employee_limits=[], shift_count=0, scheduled_shifts=[],scheduled_shifts_names=[],  authorization=0):
        self.idemployee = idemployee
        self.first_name = first_name
        self.last_name = last_name
        self.contract_shift_amount = contract_shift_amount
        self.shift_count = shift_count
        self.scheduled_shifts = scheduled_shifts
        self.scheduled_shifts_names = scheduled_shifts_names
        self.employee_limits = employee_limits
        self.authorization = authorization
        all_employees.append(self)


class Days:

    def __init__(self, day_code, day_name, all_assigned_employees=[], all_assigned_names=[], shifts=[]):
        self.day_code = day_code
        self.day_name = day_name
        self.all_assigned_employees = all_assigned_employees
        self.shifts = shifts
        self.all_assigned_names = all_assigned_names
        all_days.append(self)


class Shifts:

    def __init__(self, shift_code, shift_name, day_name, required_employees, required_authorizations, compatible_employees=[], assigned_employees=[], assigned_names=[]):
        self.shift_code = shift_code
        self.shift_name = shift_name
        self.day_name = day_name
        self.required_employees = required_employees
        self.required_authorizations = required_authorizations
        self.compatible_employees = compatible_employees
        self.assigned_employees = assigned_employees
        self.assigned_names = assigned_names
        all_shifts.append(self)


# def choose_an_employee():
#     while True:
#         selected_employee = random.choice(all_employees)
#         if selected_employee not in excluded_employees_from_regular_shifts:
#             break
#     return selected_employee
#
#
# def choose_a_supervisor():
#     while True:
#         selected_supervisor = random.choice(excluded_employees_from_regular_shifts)
#         if selected_supervisor.name != 'PlaceHolder':
#             break
#     return selected_supervisor
#
#
# def assign_protools():
#     for shift in all_shifts:
#         if shift.is_protools_required is True:
#             while len(shift.assigned_employees) < shift.required_employees:
#                 for employee in all_employees:
#                     if employee not in excluded_employees_from_regular_shifts:
#                         if employee.is_protools_authorized is True and employee.shift_count > 0:
#                             if shift.shift_code in employee.employee_limits:
#                                 shift.assigned_employees.append(all_employees[-1])
#                                 shift.assigned_names.append(all_employees[-1].name)
#                                 all_employees[-1].scheduled_shifts.append(shift)
#                                 all_employees[-1].scheduled_shifts_names.extend([shift.day_name, shift.shift_name])
#                                 all_employees[-1].shift_count -= 1
#                                 # day.all_assigned_employees.append(all_employees[-1])
#                                 # day.all_assigned_names.append(all_employees[-1])
#                             else:
#                                 shift.assigned_employees.append(employee)
#                                 shift.assigned_names.append(employee.name)
#                                 employee.shift_count -= 1
#                                 for day in all_days:
#                                     if day.day_name == shift.day_name:
#                                         day.all_assigned_employees.append(employee)
#                                         day.all_assigned_names.append(employee.name)
#                                         employee.scheduled_shifts.append(shift)
#                                         employee.scheduled_shifts_names.extend([shift.day_name, shift.shift_name])
#
#
# def assign_supervisor():
#     for day in all_days:
#         for shift in day.shifts:
#             if shift.shift_name == 'Super Morning' or shift.shift_name == 'Super Evening':
#                 while len(shift.assigned_employees) < shift.required_employees:
#                     selected_employee = choose_a_supervisor()
#                     if not selected_employee.shift_count <= 0 and shift.shift_code not in selected_employee.employee_limits:
#                         if selected_employee in shift.assigned_employees:
#                             pass
#                         elif selected_employee in day.all_assigned_employees:
#                             pass
#                         else:
#                             shift.assigned_employees.append(selected_employee)
#                             day.all_assigned_employees.append(selected_employee)
#                             shift.assigned_names.append(selected_employee.name)
#                             day.all_assigned_names.append(selected_employee.name)
#                             selected_employee.scheduled_shifts.append(shift)
#                             selected_employee.scheduled_shifts_names.extend([shift.day_name, shift.shift_name])
#                             selected_employee.shift_count -= 1




class DbHandler:

    def __init__(self):

        self.connection = sqlcon.connect(host='localhost', user='zem', password='Zemer123!@#', database='scheduler')
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(dictionary=True)

    def show_all_employees(self):
        self.cursor.execute('SELECT * FROM employee')
        data = self.cursor.fetchall()
        for row in data:
            print(row)

    def db_insert_employee(self, employee_first_name, employee_last_name):
        self.cursor.execute('INSERT INTO employee (employee_first_name, employee_last_name) VALUES (%s, %s)',
                            (employee_first_name, employee_last_name))
        self.connection.commit()

    def db_delete_employee_by_name(self, employee_first_name, employee_last_name):
        self.cursor.execute('DELETE FROM employee WHERE employee_first_name=%s AND employee_last_name=%s',
                            (employee_first_name, employee_last_name))
        self.connection.commit()

    def db_delete_employee_by_id(self, ids):
        self.cursor.execute('DELETE FROM employee WHERE ID="%s"', ids)
        self.connection.commit()

    def db_random_query(self, query, args):
        self.cursor.execute(query, args)
        self.connection.commit()

    def db_get_employee_names(self):
        self.cursor.execute('SELECT employee_first_name, employee_last_name FROM employee;')
        data = self.cursor.fetchall()
        for row in data:
            print(row)


    def db_get_employees(self):
        self.cursor.execute('SELECT idemployee, employee_first_name, employee_last_name,'
                            ' contract_shift_amount FROM employee')
        data = self.cursor.fetchall()
        for a, b, c, d in data:
            print(a, b, c, d)
            Employee(a, b, c, d)
        print(all_employees)

    def db_employee_authorizations(self):
        self.cursor.execute('SELECT idemployee, idauthorization FROM employee_authorization')
        data = self.cursor.fetchall()
        for row in data:
            print(row)
        for emp in all_employees:
            for a, b in data:
                if emp.idemployee == a:
                    emp.authorization = b

    def db_employee_limits(self):
        self.cursor.execute('SELECT idemployee, idshift FROM employee_limit')
        data = self.cursor.fetchall()
        for employee in all_employees:
            for a, b in data:
                if employee.idemployee == a:
                    employee.employee_limits.append(b)



    def db_get_days(self):
        self.cursor.execute('SELECT idday, day_name FROM day')
        data = self.cursor.fetchall()
        for a, b in data:
            print(a, b)
            Days(a, b)
        print(all_days)

    def db_get_shifts(self):
        self.cursor.execute('SELECT idshift, shift_name, idday, shift_required_employees,'
                            'shift_required_authorizations FROM shift')
        data = self.cursor.fetchall()
        for a, b, c, d, e in data:
            Shifts(a, b, c, d, e)
        print(all_shifts)



    def __del__(self):
        # self.cursor.close()
        self.connection.close()


handler = DbHandler()


def make_employees():
    handler.db_get_employees()
    handler.db_employee_authorizations()
    handler.db_employee_limits()




def create_universe():
    make_employees()
    handler.db_get_days()
    handler.db_get_shifts()
    for emp in all_employees:
        print(emp.first_name, emp.last_name, emp.authorization, emp.employee_limits)



def find_compatible_employees():
    for shift in all_shifts:
        for employee in all_employees:
            if shift.required_authorizations == employee.authorization:
                shift.compatible_employees.append(employee)

find_compatible_employees()

def assign_employees2():
        for shift in all_shifts:
            while len(shift.assigned_employees) < shift.required_employees:
                selected_employee = random.choice(shift.compatible_employees)
                if not selected_employee.shift_count >= employee.contract_shift_amount and shift.shift_code not in selected_employee.employee_limits:
                    if selected_employee in shift.assigned_employees:
                        pass
                    # elif selected_employee in day.all_assigned_employees:
                    #     pass
                    else:
                        shift.assigned_employees.append(selected_employee)
                        # day.all_assigned_employees.append(selected_employee)
                        shift.assigned_names.append(selected_employee.first_name + " " + selected_employee.last_name)
                        # day.all_assigned_names.append(selected_employee.name)
                        selected_employee.scheduled_shifts.append(shift)
                        selected_employee.scheduled_shifts_names.extend([shift.day_name, shift.shift_name])
                        selected_employee.shift_count -= 1
                else:
                    pass



# def assign_employees():
#     for day in all_days:
#         for shift in day.shifts:
#             if shift.shift_name != 'Protools':
#                 while len(shift.assigned_employees) < shift.required_employees:
#                     selected_employee = choose_an_employee()
#                     if selected_employee in excluded_employees_from_regular_shifts:
#                         pass
#                     elif not selected_employee.shift_count <= 0 and shift.shift_code not in selected_employee.employee_limits:
#                         if selected_employee in shift.assigned_employees:
#                             pass
#                         elif selected_employee in day.all_assigned_employees:
#                             pass
#                         else:
#                             shift.assigned_employees.append(selected_employee)
#                             day.all_assigned_employees.append(selected_employee)
#                             shift.assigned_names.append(selected_employee.name)
#                             day.all_assigned_names.append(selected_employee.name)
#                             selected_employee.scheduled_shifts.append(shift)
#                             selected_employee.scheduled_shifts_names.extend([shift.day_name, shift.shift_name])
#                             selected_employee.shift_count -= 1
#                     else:
#                         pass


def check_wrongful_assignment():
    for shift in all_shifts:
        for employee in shift.assigned_employees:
            if shift.shift_code in employee.employee_limits:
                shift.assigned_employees.remove(employee)
                shift.assigned_names.remove(employee.name)
                shift.assigned_employees.append(all_employees[-1])
                shift.assigned_names.append(all_employees[-1].name)
                print('Attention! Wrongful Assignment!!')


def check_remaining_employees():
    print('Remaining Employees:')
    for employee in all_employees:
        if employee.shift_count > 0:
            print(employee.name, '=>', str(employee.shift_count), 'Remaining Shifts')


def check_shift_amount():
    shifts_total = sum(shift.required_employees for shift in all_shifts)
    print('Total Required Employees', shifts_total)
    return shifts_total


def check_employee_amount():
    total_employee_amount = sum(employee.contract_shift_amount for employee in all_employees)
    print('Total Available Employees', total_employee_amount)
    return total_employee_amount


def are_there_enough_employees():
    total_employee_amount = check_employee_amount()
    total_shift_amount = check_shift_amount()
    if total_shift_amount - total_employee_amount > 0:
        print('Not Enough Employees! Please Hire More!!')
        return False
    else:
        print('There are enough employees to complete the schedule')
        return True


def show_schedule():
    for shift in all_shifts:
        print(shift.day_name, shift.shift_name, shift.assigned_names)
    # for shift in all_shifts:
    #     return str(shift.day_name, shift.shift_name), shift.assigned_names


# def save_schedule_as_excel():
#     wb = Workbook('utf-8')
#     sheet1 = wb.add_sheet('Sheet 1')
#     for row_number, shift in enumerate(all_shifts):
#         sheet1.write(row_number, 0, str(shift.day_name+shift.shift_name))
#         sheet1.write(row_number, 1, str(shift.assigned_names))
#
#     for row_number1, employee in enumerate(all_employees):
#         sheet1.write(row_number1, 3, str(employee.name))
#         sheet1.write(row_number1, 4, str(employee.scheduled_shifts_names))
#
#     sheet1.col(0).width = 4000
#     sheet1.col(1).width = 4000
#     sheet1.col(2).width = 4000
#     sheet1.col(3).width = 4000
#     sheet1.col(4).width = 4000
#
#     wb.save('test.xls')


def run():
    is_schedule_possible = are_there_enough_employees()
    if is_schedule_possible is True:
        # check_shift_amount()
        # check_employee_amount()
        # assign_protools()
        # assign_supervisor()
        assign_employees2()
        show_schedule()
        check_remaining_employees()


if __name__ == '__main__':
    create_universe()
    for shift in all_shifts:
        print(shift.shift_code, shift.shift_name, shift.required_authorizations)
    for employee in all_employees:
        print(employee.first_name, employee.last_name, employee.authorization)
    run()
