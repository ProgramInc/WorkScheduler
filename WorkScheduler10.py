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

    def __init__(self, day_name, all_assigned_employees=[]):
        self.day_name = day_name
        self.all_assigned_employees = all_assigned_employees


    class Shifts:
        all_shifts = []

        def __init__(self, day_name, shift_name, required_employees, assigned_employees=[], is_protools_required=False):
            self.day_name = day_name
            self.shift_name = shift_name
            self.required_employees = required_employees
            self.assigned_employees = assigned_employees
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
                        shift.assigned_employees.append(employee.name)
                        employee.shift_count -= 1
                        for day in Days.all_days:
                            if day.day_name == shift.day_name:
                                day.all_assigned_employees.append(employee.name)
                    # else:
                    #     shift.assigned_employees.append('filler')

def assign_employees():
    for shift in Days.Shifts.all_shifts:
        while len(shift.assigned_employees) < shift.required_employees:
            selected_employee = choose_an_employee()
            if selected_employee.name not in shift.assigned_employees and selected_employee.shift_count > 0:
                shift.assigned_employees.append(selected_employee.name)
                selected_employee.shift_count -= 1
                for day in Days.all_days:
                    if day.day_name == shift.day_name:
                        day.all_assigned_employees.append(selected_employee.name)

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

day1 = Days('Sunday', [])
day2 = Days('Monday', [])
day3 = Days('Tuesday', [])
day4 = Days('Wednesday', [])
day5 = Days('Thursday', [])
day6 = Days('Friday', [])
day7 = Days('Saturday', [])


day1shift1 = Days.Shifts('Sunday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day1shift2 = Days.Shifts('Sunday', 'Protools', required_employees=1, assigned_employees=[], is_protools_required=True)
day1shift3 = Days.Shifts('Sunday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day1shift4 = Days.Shifts('Sunday', 'Arabic', required_employees=1, assigned_employees=[], is_protools_required=False)
day1shift5 = Days.Shifts('Sunday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day1shift6 = Days.Shifts('Sunday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day2shift1 = Days.Shifts('Monday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day2shift2 = Days.Shifts('Monday', 'Protools', required_employees=1, assigned_employees=[], is_protools_required=True)
day2shift3 = Days.Shifts('Monday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day2shift4 = Days.Shifts('Monday', 'Arabic', required_employees=1, assigned_employees=[], is_protools_required=False)
day2shift5 = Days.Shifts('Monday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day2shift6 = Days.Shifts('Monday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day3shift1 = Days.Shifts('Tuesday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day3shift2 = Days.Shifts('Tuesday', 'Protools', required_employees=1, assigned_employees=[], is_protools_required=True)
day3shift3 = Days.Shifts('Tuesday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day3shift4 = Days.Shifts('Tuesday', 'Arabic', required_employees=1, assigned_employees=[], is_protools_required=False)
day3shift5 = Days.Shifts('Tuesday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day3shift6 = Days.Shifts('Tuesday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day4shift1 = Days.Shifts('Wednesday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day4shift2 = Days.Shifts('Wednesday', 'Protools', required_employees=1, assigned_employees=[], is_protools_required=True)
day4shift3 = Days.Shifts('Wednesday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day4shift4 = Days.Shifts('Wednesday', 'Arabic', required_employees=1, assigned_employees=[], is_protools_required=False)
day4shift5 = Days.Shifts('Wednesday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day4shift6 = Days.Shifts('Wednesday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day5shift1 = Days.Shifts('Thursday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day5shift2 = Days.Shifts('Thursday', 'Protools', required_employees=1, assigned_employees=[], is_protools_required=True)
day5shift3 = Days.Shifts('Thursday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day5shift4 = Days.Shifts('Thursday', 'Arabic', required_employees=1, assigned_employees=[], is_protools_required=False)
day5shift5 = Days.Shifts('Thursday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day5shift6 = Days.Shifts('Thursday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day6shift1 = Days.Shifts('Friday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day6shift2 = Days.Shifts('Friday', 'Protools', required_employees=0, assigned_employees=[], is_protools_required=False)
day6shift3 = Days.Shifts('Friday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day6shift4 = Days.Shifts('Friday', 'Arabic', required_employees=0, assigned_employees=[], is_protools_required=False)
day6shift5 = Days.Shifts('Friday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day6shift6 = Days.Shifts('Friday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

day7shift1 = Days.Shifts('Saturday', 'Morning', required_employees=2, assigned_employees=[], is_protools_required=False)
day7shift2 = Days.Shifts('Saturday', 'Protools', required_employees=0, assigned_employees=[], is_protools_required=False)
day7shift3 = Days.Shifts('Saturday', 'Turner', required_employees=0, assigned_employees=[], is_protools_required=False)
day7shift4 = Days.Shifts('Saturday', 'Arabic', required_employees=0, assigned_employees=[], is_protools_required=False)
day7shift5 = Days.Shifts('Saturday', 'Evening', required_employees=2, assigned_employees=[], is_protools_required=False)
day7shift6 = Days.Shifts('Saturday', 'Night', required_employees=0, assigned_employees=[], is_protools_required=False)

# print(Days.Shifts.all_shifts)
assign_protools()
assign_employees()
for shift in Days.Shifts.all_shifts:
    print(shift.day_name+shift.shift_name+str(shift.assigned_employees))
# print(day1shift1.assigned_employees)