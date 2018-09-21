import unittest
import WorkScheduler8

class SchedulerTester(unittest.TestCase):


    def setUp(self):
        WorkScheduler8.sunday_protools(1)

    def test_sunday_protools_is_correct_employy_amount(self):
        '''This test checks if the function sunday_protools() outputs the correct
        amount of employees - This test is meant to pass'''
        self.assertEqual(len(WorkScheduler8.SundayProtools), WorkScheduler8.sunday_protools.employee_amount.get('x'))

    def test_sundayprotools_change_expected_result_and_test_again(self):
        '''This test adds another employee to the list SundayProtools and then
        checks if the amount is correct- This test is meant to fail'''
        WorkScheduler8.SundayProtools.append('Zemer')
        self.assertEqual(len(WorkScheduler8.SundayProtools), WorkScheduler8.sunday_protools.employee_amount.get('x'))
        WorkScheduler8.SundayProtools.remove('Zemer')

    def test_is_employee_qualified_for_protools_shift(self):
        '''This test will check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift - This test is meant to pass'''
        for name in WorkScheduler8.SundayProtools:
            self.assertIn(name, (WorkScheduler8.proTools))

    @unittest.skip('ruins the other tests')
    def test_is_an_unqualified_employee_qualified_for_protools_shift(self):
        '''This test adds an unqualified employee to the list SundayProtools and will then
        check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift - This test is meant to fail'''
        WorkScheduler8.SundayProtools.append('Zemer')
        for name in WorkScheduler8.SundayProtools:
            self.assertIn(name, (WorkScheduler8.proTools))

    def test_is_any_name_listed_twice_in_SundayProtools(self):
        '''This test checks if any name appears more than once in SundayProotls.
        The logic behind the test is that it uses the SET propeties(no duplicates) and then
        complares the length of the list SundayProtools to the lengh of the set(SundayProtools)
        '''
        self.assertEqual(len(WorkScheduler8.SundayProtools), len(list(set(WorkScheduler8.SundayProtools))))
        
        
