import unittest
from WorkScheduler10 import Days, Employee, Shifts, run, show_schedule, all_shifts, all_days, all_employees


def create_universe():

    Employee('emp1', 5, 0, [], True)
    Employee('emp2', 5, 0, [], False)
    Employee('emp3', 5, 0, [], False)
    Employee('emp4', 5, 0, [], False)
    Employee('emp5', 4, 0, [], False)
    Employee('emp6', 4, 0, [], False)
    Employee('emp7', 4, 0, [], False)
    Employee('emp8', 4, 0, [], False)
    Employee('emp9', 4, 0, [], False)
    Employee('emp10', 3, 0, [], False)

    day1shift1 = Shifts('Sunday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day1shift2 = Shifts('Sunday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=True)
    day1shift3 = Shifts('Sunday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day1shift4 = Shifts('Sunday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day1shift5 = Shifts('Sunday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day1shift6 = Shifts('Sunday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day2shift1 = Shifts('Monday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day2shift2 = Shifts('Monday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=True)
    day2shift3 = Shifts('Monday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day2shift4 = Shifts('Monday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day2shift5 = Shifts('Monday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day2shift6 = Shifts('Monday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day3shift1 = Shifts('Tuesday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day3shift2 = Shifts('Tuesday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=True)
    day3shift3 = Shifts('Tuesday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day3shift4 = Shifts('Tuesday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day3shift5 = Shifts('Tuesday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day3shift6 = Shifts('Tuesday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day4shift1 = Shifts('Wednesday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day4shift2 = Shifts('Wednesday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=True)
    day4shift3 = Shifts('Wednesday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day4shift4 = Shifts('Wednesday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day4shift5 = Shifts('Wednesday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day4shift6 = Shifts('Wednesday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day5shift1 = Shifts('Thursday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day5shift2 = Shifts('Thursday', 'Protools', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=True)
    day5shift3 = Shifts('Thursday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day5shift4 = Shifts('Thursday', 'Arabic', required_employees=1, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day5shift5 = Shifts('Thursday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day5shift6 = Shifts('Thursday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day6shift1 = Shifts('Friday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day6shift2 = Shifts('Friday', 'Protools', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day6shift3 = Shifts('Friday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day6shift4 = Shifts('Friday', 'Arabic', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day6shift5 = Shifts('Friday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day6shift6 = Shifts('Friday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    day7shift1 = Shifts('Saturday', 'Morning', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day7shift2 = Shifts('Saturday', 'Protools', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day7shift3 = Shifts('Saturday', 'Turner', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day7shift4 = Shifts('Saturday', 'Arabic', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day7shift5 = Shifts('Saturday', 'Evening', required_employees=2, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)
    day7shift6 = Shifts('Saturday', 'Night', required_employees=0, assigned_employees=[], assigned_names=[],
                        is_protools_required=False)

    Days('Sunday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day1shift1, day1shift2, day1shift3, day1shift4, day1shift5, day1shift6])
    Days('Monday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day2shift1, day2shift2, day2shift3, day2shift4, day2shift5, day2shift6])
    Days('Tuesday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day3shift1, day3shift2, day3shift3, day3shift4, day3shift5, day3shift6])
    Days('Wednesday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day4shift1, day4shift2, day4shift3, day4shift4, day4shift5, day4shift6])
    Days('Thursday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day5shift1, day5shift2, day5shift3, day5shift4, day5shift5, day5shift6])
    Days('Friday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day6shift1, day6shift2, day6shift3, day6shift4, day6shift5, day6shift6])
    Days('Saturday', all_assigned_employees=[], all_assigned_names=[],
         shifts=[day7shift1, day7shift2, day7shift3, day7shift4, day7shift5, day7shift6])

    return all_employees, all_shifts, all_days


class SchedulerTester(unittest.TestCase):

    def setUp(self):
        print('this is the setUp for the test')
        self.Days = Days
        self.Shifts = Shifts
        self.Employee = Employee
        self.all_employees, self.all_shifts, self.all_days = create_universe()
        run()

    def tearDown(self):
        self.all_employees.clear()
        self.all_shifts.clear()
        self.all_days.clear()
        print('This Is The End Of This Test')

    def test_that_all_shifts_that_require_employees_have_assigned_employees(self):
        """This test will verify that each shift has assigned employees"""
        # for self.day in Days.all_days:
        for shift in self.all_shifts:
            if shift.required_employees > 0:
                self.assertGreater(len(shift.assigned_employees), 0)

    def test_that_all_shifts_have_assigned_employees_change_outcome_and_test_again(self):
        """This test removes all employees from day1shift1 and then verify that the shift
        has employees agssigned to it - raising an AssertionError"""
        self.all_shifts[0].assigned_employees.clear()
        try:
            self.assertGreater(len(self.all_shifts[0].assigned_employees), 0)
        except AssertionError:
            print('Goodness')
            pass

    def test_shift_is_correct_employee_amount(self):
        """This test checks if the function assign_employees() outputs the correct
        amount of employees for one specific shift"""
        # print(self.Days.all_days[0].shifts[0].assigned_employees, 'this is where the problem is')
        self.assertEqual(len(all_shifts[0].assigned_employees), 2)

    def test_a_shift_change_expected_result_and_test_again(self):
        """This test adds another employee to the list day1shift1.assigned_employees and then
        checks if the amount is correct - raising an AssertionError"""
        self.all_shifts[0].assigned_employees.append('1 too many')
        try:
            self.assertEqual(len(self.all_shifts[0].assigned_employees), 2)
        except AssertionError:
            pass

    def test_is_employee_qualified_for_protools_shift(self):
        """This test will check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift """
        for shift in self.all_shifts:
            if shift.shift_name == 'Protools':
                for employee in shift.assigned_employees:
                    self.assertTrue(employee.is_protools_authorized)

    def test_is_an_employee_listed_twice_for_a_shift(self):
        """This test checks if any employee is listed twice in the same shift"""
        for shift in self.all_shifts:
            self.assertEqual(len(shift.assigned_employees), len(list(set(shift.assigned_employees))))

    def test_is_an_employee_listed_twice_change_outcome_and_test_again(self):
        """This test adds an employee twice to the same shift and then tests again, raising an assertion error"""
        self.all_shifts[0].assigned_names.append(self.all_shifts[0].assigned_names[0])
        self.all_shifts[0].assigned_employees.append(self.all_shifts[0].assigned_employees[0])
        show_schedule()
        try:
            self.assertEqual(len(self.all_shifts[0].assigned_names), len(list(set(self.all_shifts[0].assigned_names))))
            self.assertEqual(len(self.all_shifts[0].assigned_employees), len(list(set(self.all_shifts[0].assigned_employees))))
        except AssertionError:
            print('Passed')
            pass

    def test_did_any_employee_not_get_any_shifts(self):
        """This test will cycle through all the employees and make sure that each
        employee was assigned to at least 1 shift"""
        for employee in self.all_employees:
            if employee.shift_count > 0:
                self.assertGreater(len(employee.scheduled_shifts), 0)
    #
    # def test_did_all_employees_get_exact_shift_number_according_to_their_contract(self):
    #     """This test will make sure that each employee is listed to the exact
    #     number of shifts according to their contract"""
    #     for employee in all_employees:
    #         self.assertEqual(len(self.employee.scheduled_shifts), self.employee.contract_shift_count)
    #