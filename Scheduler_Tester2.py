import unittest
import WorkScheduler10



class SchedulerTester(unittest.TestCase):

    def setUp(self):
        WorkScheduler10.assign_protools()
        WorkScheduler10.assign_employees2()

    def tearDown(self):
        pass

    def test_that_all_shifts_have_assigned_employees(self):
        """This test will verify that each shift has assigned employees"""
        for self.day in WorkScheduler10.Days.all_days:
            for self.shift in self.day.shifts:
                if self.shift.required_employees >= 1:
                    self.assertGreater(len(self.shift.assigned_employees), 0)

    def test_that_all_shifts_have_assigned_employees_change_outcome_and_test_again(self):
        """This test removes all employees from day1shift1 and then verify that the shift
        has employees agssigned to it - raising an AssertionError"""
        WorkScheduler10.Days.all_days[0].shifts[0].assigned_employees.clear()
        try:
            for shift in WorkScheduler10.Days.Shifts.all_shifts:
                self.assertGreater(len(shift.assigned_employees), 0)
        except AssertionError:
            print('Good')
            pass

    def test_shift_is_correct_employee_amount(self):
        """This test checks if the function assign_employees() outputs the correct
        amount of employees"""
        self.assertEqual(len(WorkScheduler10.Days.all_days[0].shifts[0].assigned_employees), 2)

    #
    def test_a_shift_change_expected_result_and_test_again(self):
        """This test adds another employee to the list day1shift1.assigned_employees and then
        checks if the amount is correct - raising an AssertionError"""
        WorkScheduler10.Days.all_days[0].shifts[0].assigned_employees.append('too many')
        try:
            self.assertEqual(len(WorkScheduler10.Days.all_days[0].shifts[0].assigned_employees), 2)
        except AssertionError:
            print('good')
            pass
    # #
    # def test_is_employee_qualified_for_protools_shift(self):
    #     """This test will check whether or not the employee that was assigned is in the
    #     list of qualified employees for a protools shift """
    #     for employee in self.aShift1.assigned_employees:
    #         self.assertTrue(employee.is_protools_authorized)
    #
    # def test_is_an_employee_listed_twice_for_a_shift(self):
    #     """This test checks if any employee is listed twice in the same shift"""
    #     for shift in DaysAndShifts.all_shifts:
    #         self.assertEqual(len(shift.assigned_employees), len(list(set(shift.assigned_employees))))
    #
    # def test_is_an_employee_listed_twice_change_outcome_and_test_again(self):
    #     """This test adds an employee twice to the same shift and then tests again, raising an assertion error"""
    #     self.aShift1.assigned_employees.append(self.anEmployee1)
    #     try:
    #         self.assertEqual(len(self.shift.assigned_employees), len(list(set(self.shift.assigned_employees))))
    #     except AssertionError:
    #         pass
    #
    # def test_did_any_employee_not_get_any_shifts(self):
    #     """This test will cycle through all the employees and make sure that each
    #     employee was assigned to at least 1 shift"""
    #     for employee in Employee.all_employees:
    #         self.assertGreater(len(self.employee.scheduled_shifts), 0)
    #
    # def test_did_all_employees_get_exact_shift_number_according_to_their_contract(self):
    #     """This test will make sure that each employee is listed to the exact
    #     number of shifts according to their contract"""
    #     for employee in Employee.all_employees:
    #         self.assertEqual(len(self.employee.scheduled_shifts), self.employee.contract_shift_count)
    #
