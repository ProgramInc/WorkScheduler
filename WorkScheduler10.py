class Employee:

    def __init__(self, name, shift_count, cooldown, scheduled_shifts=[], is_protools_authorized=False):
        self.name = name
        self.shift_count = shift_count
        self.cooldown = cooldown
        self.scheduled_shifts = scheduled_shifts
        self.is_protools_authorized = is_protools_authorized

    def set_cooldown_period(self, cooldown_amount):
        self.cooldown = cooldown_amount


class DaysAndShifts:

    def __init__(self, day_name, shift_name, assigned_employees=[]):
        self.day_name = day_name
        self.shift_name = shift_name
        self.assigned_employees = assigned_employees

    def assign_employee(self, Employee):
        self.assigned_employees.append(Employee)

    def unassign_employee(self):
        self.assigned_employees.remove(Employee)
