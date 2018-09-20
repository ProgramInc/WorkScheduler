import unittest
import WorkScheduler8

class SchedulerTester(unittest.TestCase):


    def setUp(self):
        WorkScheduler8.sunday_protools(1)

    def test_sunday_protools_is_correct_employy_amount(self):
        'This test checks if the function sunday_protools outputs the correct amount of employees - This test is meant to pass'
        self.assertEqual(len(WorkScheduler8.SundayProtools), WorkScheduler8.sunday_protools.employee_amount.get('x'))

    def test_sundayprotools_change_expected_result_and_test_again(self):
        'This test adds another employee to SundayProtools and then checks if the amount is correct- This test is meant to fail'
        WorkScheduler8.SundayProtools.append('Zemer')
        self.assertEqual(len(WorkScheduler8.SundayProtools), WorkScheduler8.sunday_protools.employee_amount.get('x'))
