import unittest
from WorkScheduler10 import *
# from WorkScheduler10 import assign_employees, assign_protools, Days, run




class SchedulerTester(unittest.TestCase):

    def setUp(self):
        print('this is the setUp for the test')
        run()
        self.Days = Days
        self.Employee = Employee

    def tearDown(self):
        print('This Is The End Of This Test')


    def test_that_all_shifts_that_require_employees_have_assigned_employees(self):
        """This test will verify that each shift has assigned employees"""
        for self.day in Days.all_days:
            for self.shift in self.day.shifts:
                if self.shift.required_employees > 0:
                    self.assertGreater(len(self.shift.assigned_employees), 0)

    def test_that_all_shifts_have_assigned_employees_change_outcome_and_test_again(self):
        """This test removes all employees from day1shift1 and then verify that the shift
        has employees agssigned to it - raising an AssertionError"""
        self.Days.all_days[0].shifts[0].assigned_employees.clear()
        try:
            self.assertGreater(len(Days.all_days[0].shifts[0].assigned_employees), 0)
        except AssertionError:
            print('Goodness')
            pass

    def test_shift_is_correct_employee_amount(self):
        """This test checks if the function assign_employees() outputs the correct
        amount of employees for one specific shift"""
        print(self.Days.all_days[0].shifts[0].assigned_employees, 'this is where the problem is')
        self.assertEqual(len(Days.all_days[0].shifts[0].assigned_employees), 2)

    def test_a_shift_change_expected_result_and_test_again(self):
        """This test adds another employee to the list day1shift1.assigned_employees and then
        checks if the amount is correct - raising an AssertionError"""
        self.Days.all_days[0].shifts[0].assigned_employees.append('too many')
        try:
            self.assertEqual(len(self.Days.all_days[0].shifts[0].assigned_employees), 2)
        except AssertionError:
            self.Days.all_days[0].shifts[0].assigned_employees.remove('too many')
            # this line should not be here!!


    def test_is_employee_qualified_for_protools_shift(self):
        """This test will check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift """
        for shift in Days.Shifts.all_shifts:
            if shift.shift_name == 'Protools':
                for employee in shift.assigned_employees:
                    self.assertTrue(employee.is_protools_authorized)

    def test_is_an_employee_listed_twice_for_a_shift(self):
        """This test checks if any employee is listed twice in the same shift"""
        for shift in self.Days.Shifts.all_shifts:
            self.assertEqual(len(shift.assigned_employees), len(list(set(shift.assigned_employees))))
    #
    def test_is_an_employee_listed_twice_change_outcome_and_test_again(self):
        """This test adds an employee twice to the same shift and then tests again, raising an assertion error"""
        self.Days.all_days[0].shifts[0].assigned_employees.append(self.Days.all_days[0].shifts[0].assigned_employees[0])
        try:
            self.assertEqual(len(self.Days.all_days[0].shifts[0].assigned_employees), len(list(set(self.Days.all_days[0].shifts[0].assigned_employees))))
        except AssertionError:
            self.Days.all_days[0].shifts[0].assigned_employees.remove(self.Days.all_days[0].shifts[0].assigned_employees[0])
            # This line should not be here!!
    #
    def test_did_any_employee_not_get_any_shifts(self):
        """This test will cycle through all the employees and make sure that each
        employee was assigned to at least 1 shift"""
        for employee in Employee.all_employees:
            self.assertGreater(len(employee.scheduled_shifts), 0)
    #
    # def test_did_all_employees_get_exact_shift_number_according_to_their_contract(self):
    #     """This test will make sure that each employee is listed to the exact
    #     number of shifts according to their contract"""
    #     for employee in Employee.all_employees:
    #         self.assertEqual(len(self.employee.scheduled_shifts), self.employee.contract_shift_count)
    #
