import random


class Employee:

    all_employees = []

    def __init__(self, name, shift_count, cooldown, scheduled_shifts=[], is_protools_authorized=False):
        self.name = name
        self.shift_count = shift_count
        self.cooldown = cooldown
        self.scheduled_shifts = scheduled_shifts
        self.is_protools_authorized = is_protools_authorized
        Employee.all_employees.append(self)


class Days:

    all_days = []

    def __init__(self, day_name, all_assigned_employees=[], all_assigned_names=[], shifts=[]):
        self.day_name = day_name
        self.all_assigned_employees = all_assigned_employees
        self.shifts = shifts
        self.all_assigned_names = all_assigned_names
        Days.all_days.append(self)

    class Shifts:

        all_shifts = []

        def __init__(self, day_name, shift_name, required_employees, assigned_employees=[], assigned_names=[], is_protools_required=False):
            self.day_name = day_name
            self.shift_name = shift_name
            self.required_employees = required_employees
            self.assigned_employees = assigned_employees
            self.assigned_names = assigned_names
            self.is_protools_required = is_protools_required
            Days.Shifts.all_shifts.append(self)


def choose_an_employee():
    selected_employee = random.choice(Employee.all_employees)
    return selected_employee


def assign_protools():
    for shift in Days.Shifts.all_shifts:
        if shift.is_protools_required is True:
            while len(shift.assigned_employees) < shift.required_employees:
                for employee in Employee.all_employees:
                    if employee.is_protools_authorized is True and employee.shift_count > 0:
                        shift.assigned_employees.append(employee)
                        shift.assigned_names.append(employee.name)
                        employee.shift_count -= 1
                        for day in Days.all_days:
                            if day.day_name == shift.day_name:
                                day.all_assigned_employees.append(employee)
                                day.all_assigned_names.append(employee.name)
                                employee.scheduled_shifts.append(shift)
                    # else:
                    #     shift.assigned_employees.append('filler')


def assign_employees():
    for day in Days.all_days:
        for shift in day.shifts:
            # print(selected_employee )
            while len(shift.assigned_employees) < shift.required_employees:
                selected_employee = choose_an_employee()
                if not selected_employee.shift_count <= 0:
                    if selected_employee in shift.assigned_employees:
                        pass
                    elif selected_employee in day.all_assigned_employees:
                        pass
                    else:
                        shift.assigned_employees.append(selected_employee)
                        day.all_assigned_employees.append(selected_employee)
                        shift.assigned_names.append(selected_employee.name)
                        day.all_assigned_names.append(selected_employee.name)
                        selected_employee.scheduled_shifts.append(shift)
                        selected_employee.shift_count -= 1
                else:
                    pass



def check_remaining_employees():
    print('Remaining Employees:')
    for employee in Employee.all_employees:
        if employee.shift_count > 0:
            print(employee.name, '=>', str(employee.shift_count), 'Remaining Shifts')


def check_shift_amount():
    total = []
    for day in Days.all_days:
        # for shift in day.shifts:
        day_shifts_total = sum(shift.required_employees for shift in day.shifts)
        total.append(day_shifts_total)
        print(day.day_name, 'Required Employees', day_shifts_total)
    print('Total Required Employees', sum(total))


def check_employee_amount():
    total_employee_amount = sum(employee.shift_count for employee in Employee.all_employees)
    print('Total Available Employees', total_employee_amount)


def show_schedule():
    for shift in Days.Shifts.all_shifts:
            print(shift.day_name+shift.shift_name, shift.assigned_names)


def create_universe():
    employee1 = Employee('emp1', 5, 0, [], True)
    employee2 = Employee('emp2', 5, 0, [], False)
    employee3 = Employee('emp3', 5, 0, [], False)
    employee4 = Employee('emp4', 5, 0, [], False)
    employee5 = Employee('emp5', 4, 0, [], False)
    employee6 = Employee('emp6', 4, 0, [], False)
    employee7 = Employee('emp7', 4, 0, [], False)
    employee8 = Employee('emp8', 4, 0, [], False)
    employee9 = Employee('emp9', 4, 0, [], False)
    employee10 = Employee('emp10', 3, 0, [], False)

    day1shift1 = Days.Shifts('Sunday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift2 = Days.Shifts('Sunday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=True)
    day1shift3 = Days.Shifts('Sunday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift4 = Days.Shifts('Sunday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift5 = Days.Shifts('Sunday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift6 = Days.Shifts('Sunday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day2shift1 = Days.Shifts('Monday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift2 = Days.Shifts('Monday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=True)
    day2shift3 = Days.Shifts('Monday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift4 = Days.Shifts('Monday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift5 = Days.Shifts('Monday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift6 = Days.Shifts('Monday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day3shift1 = Days.Shifts('Tuesday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift2 = Days.Shifts('Tuesday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=True)
    day3shift3 = Days.Shifts('Tuesday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift4 = Days.Shifts('Tuesday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift5 = Days.Shifts('Tuesday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift6 = Days.Shifts('Tuesday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day4shift1 = Days.Shifts('Wednesday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift2 = Days.Shifts('Wednesday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=True)
    day4shift3 = Days.Shifts('Wednesday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift4 = Days.Shifts('Wednesday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift5 = Days.Shifts('Wednesday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift6 = Days.Shifts('Wednesday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day5shift1 = Days.Shifts('Thursday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift2 = Days.Shifts('Thursday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=True)
    day5shift3 = Days.Shifts('Thursday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift4 = Days.Shifts('Thursday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift5 = Days.Shifts('Thursday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift6 = Days.Shifts('Thursday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day6shift1 = Days.Shifts('Friday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift2 = Days.Shifts('Friday', 'Protools', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift3 = Days.Shifts('Friday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift4 = Days.Shifts('Friday', 'Arabic', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift5 = Days.Shifts('Friday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift6 = Days.Shifts('Friday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day7shift1 = Days.Shifts('Saturday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift2 = Days.Shifts('Saturday', 'Protools', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift3 = Days.Shifts('Saturday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift4 = Days.Shifts('Saturday', 'Arabic', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift5 = Days.Shifts('Saturday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift6 = Days.Shifts('Saturday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[], is_protools_required=False)

    day1 = Days('Sunday', all_assigned_employees=[], all_assigned_names=[], shifts=[day1shift1, day1shift2, day1shift3, day1shift4, day1shift5, day1shift6])
    day2 = Days('Monday', all_assigned_employees=[], all_assigned_names=[], shifts=[day2shift1, day2shift2, day2shift3, day2shift4, day2shift5, day2shift6])
    day3 = Days('Tuesday', all_assigned_employees=[], all_assigned_names=[], shifts=[day3shift1, day3shift2, day3shift3, day3shift4, day3shift5, day3shift6])
    day4 = Days('Wednesday', all_assigned_employees=[], all_assigned_names=[], shifts=[day4shift1, day4shift2, day4shift3, day4shift4, day4shift5, day4shift6])
    day5 = Days('Thursday', all_assigned_employees=[], all_assigned_names=[], shifts=[day5shift1, day5shift2, day5shift3, day5shift4, day5shift5, day5shift6])
    day6 = Days('Friday', all_assigned_employees=[], all_assigned_names=[], shifts=[day6shift1, day6shift2, day6shift3, day6shift4, day6shift5, day6shift6])
    day7 = Days('Saturday', all_assigned_employees=[], all_assigned_names=[],shifts=[day7shift1, day7shift2, day7shift3, day7shift4, day7shift5, day7shift6])



def run():
    # create_universe()
    # check_shift_amount()
    # check_employee_amount()
    assign_protools()
    assign_employees()
    show_schedule()
    # check_remaining_employees()

if __name__ == '__main__':
    run()


