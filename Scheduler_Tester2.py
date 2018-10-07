import unittest
from WorkScheduler10 import Employee, DaysAndShifts


class SchedulerTester(unittest.TestCase):

    def setUp(self):
        self.anEmployee1 = Employee(name='employee1', shift_count=5, cooldown=0, scheduled_shifts=[], is_protools_authorized=True)
        self.anEmployee2 = Employee(name='employee2', shift_count=3, cooldown=0, scheduled_shifts=[], is_protools_authorized=False)
        self.aShift1 = DaysAndShifts(day_name='aDay1', shift_name='aShift1', assigned_employees=[])
        self.aShift2 = DaysAndShifts(day_name='aDay2', shift_name='aShift2', assigned_employees=[])
        self.aShift1.assign_employee(self.anEmployee1)
        self.aShift1.assign_employee(self.anEmployee2)
        self.anEmployee1.cooldown = 3


    def tearDown(self):
        pass

    def test_that_aShift1_dot_assigned_employees_is_not_an_empty_list(self):
        """This test will verify that the list sundayProtools.assigned_employees is not empty"""
        self.assertGreater(len(self.aShift1.assigned_employees), 0)


    def test_aShift1_is_correct_employee_amount(self):
        """This test checks if the method shift.assign_employee() outputs the correct
        amount of employees"""
        self.aShift1.assign_employee(self.anEmployee2)
        self.assertEqual(len(self.aShift1.assigned_employees), 2)


    def test_a_shift_change_expected_result_and_test_again(self):
        """This test adds another employee to the list aShift1.assigned_employees and then
        checks if the amount is correct - This test is meant to raise an AssertionError"""
        self.aShift1.assigned_employees.append(self.anEmployee2)
        try:
            self.assertEqual(len(self.aShift1.assigned_employees), 1)
        except AssertionError:
                pass
    #
    def test_is_employee_qualified_for_protools_shift(self):
        """This test will check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift """
        for employee in self.aShift1.assigned_employees:
            self.assertTrue(employee.is_protools_authorized)

    def test_is_an_employee_listed_twice_for_a_shift(self):
        """This test checks if any employee is listed twice in the same shift"""
        for shift in DaysAndShifts.all_shifts:
            self.assertEqual(len(self.shift.assigned_employees), len(list(set(self.shift.assigned_employees))))

    def test_did_any_employee_not_get_any_shifts(self):
        """This test will cycle through all the employees and make sure that each
        employee was assigned to at least 1 shift"""
        for employee in Employee.all_employees:
            self.assertGreater(len(self.employee.scheduled_shifts), 0)

    def test_did_all_employees_get_exact_shift_number_according_to_their_contract(self):
        """This test will make sure that each employee is listed to the exact
        number of shifts according to their contract"""
        for employee in Employee.all_employees:
            self.assertEqual(len(self.employee.scheduled_shifts), self.employee.contract_shift_count)

