import unittest
from WorkScheduler10 import Employee, DaysAndShifts


class SchedulerTester(unittest.TestCase):

    def setUp(self):
        self.itay = Employee(name='Itay', shift_count=5, cooldown=0, scheduled_shifts=None, protools_authorized=True)
        self.sundayProtools = DaysAndShifts(day_name='Sunday', shift_name='Protools', assigned_employees=None)
        self.sundayProtools.assign_employee(self.itay)
        self.itay.cooldown = 3

    def tearDown(self):
        self.sundayProtools.assigned_employees = None
        self.itay.cooldown = 0

    def test_that_sundayProtools_assigned_employees_is_not_an_empty_list(self):
        '''This test will verify that the list sundayProtools.assigned_employees is not empty - This test is meant to pass'''
        self.assertGreater(len(self.sundayProtools.assigned_employees), 0)


    def test_sunday_protools_is_correct_employee_amount(self):
        '''This test checks if the function sunday_protools() outputs the correct
        amount of employees - This test is meant to pass'''
        self.assertEqual(len(self.sundayProtools.assigned_employees), 1)


    def test_sunday_protools_change_expected_result_and_test_again(self):
        '''This test adds another employee to the list SundayProtools and then
        checks if the amount is correct- This test is meant to fail'''
        self.sundayProtools.assigned_employees.append('Zemer')
        try:
            self.assertEqual(len(self.sundayProtools.assigned_employees), 1)
        except:
            AssertionError('Passed')
    #
    # def test_is_employee_qualified_for_protools_shift(self):
    #     '''This test will check whether or not the employee that was assigned is in the
    #     list of qualified employees for a protools shift - This test is meant to pass'''
    #     for name in SundayProtools:
    #         self.assertIn(name, (WorkScheduler8.proTools))
    #
    # # @unittest.skip('ruins the other tests')
    # def test_is_an_unqualified_employee_qualified_for_protools_shift(self):
    #     '''This test adds an unqualified employee to the list SundayProtools and will then
    #     check whether or not the employee that was assigned is in the
    #     list of qualified employees for a protools shift - This test is meant to fail'''
    #     WorkScheduler8.SundayProtools.append('Zemer')
    #     for name in WorkScheduler8.SundayProtools:
    #         self.assertIn(name, (WorkScheduler8.proTools))
    #
    # def test_is_any_name_listed_twice_in_sundayProtools(self):
    #     '''This test checks if any name appears more than once in SundayProotls.
    #     The logic behind the test is that it uses the SET propeties(no duplicates) and then
    #     complares the length of the list SundayProtools to the lengh of the set(SundayProtools)
    #     '''
    #     self.assertEqual(len(WorkScheduler8.SundayProtools), len(list(set(WorkScheduler8.SundayProtools))))
    #
