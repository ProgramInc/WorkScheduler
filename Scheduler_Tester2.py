import unittest
from WorkScheduler10 import Days, Employee, Shifts, run, show_schedule, all_shifts, all_days, all_employees,are_there_enough_employees, save_schedule_as_excel, check_wrongful_assignment
import xlrd


def create_universe():

    Employee(name='emp1', contract_shift_amount=5, shift_count=5, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=True)
    Employee(name='emp2', contract_shift_amount=5, shift_count=5, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp3', contract_shift_amount=5, shift_count=5, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp4', contract_shift_amount=5, shift_count=5, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp5', contract_shift_amount=4, shift_count=4, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp6', contract_shift_amount=4, shift_count=4, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp7', contract_shift_amount=4, shift_count=4, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp8', contract_shift_amount=4, shift_count=4, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp9', contract_shift_amount=4, shift_count=4, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='emp10', contract_shift_amount=3, shift_count=3, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)
    Employee(name='PlaceHolder', contract_shift_amount=5, shift_count=5, cooldown=0, scheduled_shifts=[], employee_limits=[],
             is_protools_authorized=False)

    day1shift1 = Shifts('Sunday', 'Morning', shift_code='Sunday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift2 = Shifts('Sunday', 'Protools', shift_code='Sunday Morning', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=True)
    day1shift3 = Shifts('Sunday', 'Turner', shift_code='Sunday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift4 = Shifts('Sunday', 'Arabic', shift_code='Sunday Evening', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift5 = Shifts('Sunday', 'Evening', shift_code='Sunday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day1shift6 = Shifts('Sunday', 'Night', shift_code='Sunday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day2shift1 = Shifts('Monday', 'Morning', shift_code='Monday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift2 = Shifts('Monday', 'Protools', shift_code='Monday Morning', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=True)
    day2shift3 = Shifts('Monday', 'Turner', shift_code='Monday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift4 = Shifts('Monday', 'Arabic', shift_code='Monday Evening', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift5 = Shifts('Monday', 'Evening', shift_code='Monday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day2shift6 = Shifts('Monday', 'Night', shift_code='Monday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day3shift1 = Shifts('Tuesday', 'Morning', shift_code='Tuesday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift2 = Shifts('Tuesday', 'Protools', shift_code='Tuesday Morning', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=True)
    day3shift3 = Shifts('Tuesday', 'Turner', shift_code='Tuesday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift4 = Shifts('Tuesday', 'Arabic', shift_code='Tuesday Evening', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift5 = Shifts('Tuesday', 'Evening', shift_code='Tuesday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day3shift6 = Shifts('Tuesday', 'Night', shift_code='Tuesday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day4shift1 = Shifts('Wednesday', 'Morning', shift_code='Wednesday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift2 = Shifts('Wednesday', 'Protools', shift_code='Wednesday Morning', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=True)
    day4shift3 = Shifts('Wednesday', 'Turner', shift_code='Wednesday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift4 = Shifts('Wednesday', 'Arabic', shift_code='Wednesday Evening', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift5 = Shifts('Wednesday', 'Evening', shift_code='Wednesday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day4shift6 = Shifts('Wednesday', 'Night', shift_code='Wednesday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day5shift1 = Shifts('Thursday', 'Morning', shift_code='Thursday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift2 = Shifts('Thursday', 'Protools', shift_code='Thursday Morning', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=True)
    day5shift3 = Shifts('Thursday', 'Turner', shift_code='Thursday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift4 = Shifts('Thursday', 'Arabic', shift_code='Thursday Evening', required_employees=1,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift5 = Shifts('Thursday', 'Evening', shift_code='Thursday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day5shift6 = Shifts('Thursday', 'Night', shift_code='Thursday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day6shift1 = Shifts('Friday', 'Morning', shift_code='Friday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift2 = Shifts('Friday', 'Protools', shift_code='Friday Morning', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift3 = Shifts('Friday', 'Turner', shift_code='Friday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift4 = Shifts('Friday', 'Arabic', shift_code='Friday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift5 = Shifts('Friday', 'Evening', shift_code='Friday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day6shift6 = Shifts('Friday', 'Night', shift_code='Friday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

    day7shift1 = Shifts('Saturday', 'Morning', shift_code='Saturday Morning', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift2 = Shifts('Saturday', 'Protools', shift_code='Saturday Morning', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift3 = Shifts('Saturday', 'Turner', shift_code='Saturday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift4 = Shifts('Saturday', 'Arabic', shift_code='Saturday Evening', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift5 = Shifts('Saturday', 'Evening', shift_code='Saturday Evening', required_employees=2,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)
    day7shift6 = Shifts('Saturday', 'Night', shift_code='Saturday Night', required_employees=0,
                        assigned_employees=[], assigned_names=[], is_protools_required=False)

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

    def tearDown(self):
        self.all_employees.clear()
        self.all_shifts.clear()
        self.all_days.clear()
        print('This Is The End Of This Test')

    def test_that_all_shifts_that_require_employees_have_assigned_employees(self):
        """This test will verify that each shift has assigned employees"""
        run()
        for shift in self.all_shifts:
            if shift.required_employees > 0:
                self.assertGreater(len(shift.assigned_employees), 0)

    def test_that_all_shifts_have_assigned_employees_change_outcome_and_test_again(self):
        """This test removes all employees from day1shift1 and then verify that the shift
        has employees agssigned to it - raising an AssertionError"""
        run()
        self.all_shifts[0].assigned_employees.clear()
        try:
            self.assertGreater(len(self.all_shifts[0].assigned_employees), 0)
        except AssertionError:
            print('Goodness')
            pass

    def test_shift_is_correct_employee_amount(self):
        """This test checks if the function assign_employees() outputs the correct
        amount of employees for one specific shift"""
        run()
        self.assertEqual(len(all_shifts[0].assigned_employees), 2)

    def test_a_shift_change_expected_result_and_test_again(self):
        """This test adds another employee to the list day1shift1.assigned_employees and then
        checks if the amount is correct - raising an AssertionError"""
        run()
        self.all_shifts[0].assigned_employees.append('1 too many')
        try:
            self.assertEqual(len(self.all_shifts[0].assigned_employees), 2)
        except AssertionError:
            pass

    def test_is_employee_qualified_for_protools_shift(self):
        """This test will check whether or not the employee that was assigned is in the
        list of qualified employees for a protools shift """
        run()
        for shift in self.all_shifts:
            if shift.shift_name == 'Protools':
                for employee in shift.assigned_employees:
                    if employee.name != "PlaceHolder":
                        self.assertTrue(employee.is_protools_authorized)

    def test_is_an_employee_listed_twice_for_a_shift(self):
        """This test checks if any employee is listed twice in the same shift"""
        run()
        for shift in self.all_shifts:
            self.assertEqual(len(shift.assigned_employees), len(list(set(shift.assigned_employees))))

    def test_is_an_employee_listed_twice_change_outcome_and_test_again(self):
        """This test adds an employee twice to the same shift and then tests again, raising an assertion error"""
        run()
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
        run()
        for employee in self.all_employees:
            if employee.contract_shift_amount > 0:
                if employee.name != 'PlaceHolder':
                    self.assertGreater(len(employee.scheduled_shifts), 0)

    def test_with_no_employees(self):
        """tests how the code behaves when there are not enough employees"""
        self.all_employees.clear()
        run()
        for shift in all_shifts:
            self.assertEqual(shift.assigned_employees, [])
            self.assertEqual(shift.assigned_names, [])

    def test_is_schedule_possible(self):
        """Checks if the function are_there_enough_employees is outputting correctly"""
        self.all_employees.clear()
        check = are_there_enough_employees()
        self.assertEqual(check, False)

    def test_protools_limits_are_working(self):
        self.all_employees[0].employee_limits.append('Sunday Morning')
        run()
        self.assertNotEqual(str(all_shifts[1].assigned_names), str(['emp1']))
        self.assertEqual(str(all_shifts[1].assigned_names), str(['PlaceHolder']))

    # def test_assignment_limits(self):
    #     self.all_employees[0].employee_limits.append('')

    def test_save_to_excel(self):
        """How do i test for this??"""
        run()
        save_schedule_as_excel()

        self.workbook = xlrd.open_workbook('test.xls')
        self.worksheet = self.workbook.sheet_by_name('Sheet 1')

        self.cell_to_check1 = self.worksheet.cell_value(0, 0)
        self.cell_to_check2 = self.worksheet.cell_value(2, 1)
        self.cell_to_check3 = self.worksheet.cell_value(7, 1)

        self.assertEqual(str(self.cell_to_check1), str('SundayMorning'))
        self.assertEqual(str(self.cell_to_check2), str('[]'))
        self.assertEqual(str(self.cell_to_check3), str(['emp1']))

    def test_save_to_excel_with_employee_limit(self):
        self.all_employees[0].employee_limits.append('Sunday Morning')

        run()
        save_schedule_as_excel()

        self.workbook = xlrd.open_workbook('test.xls')
        self.worksheet = self.workbook.sheet_by_name('Sheet 1')
        self.cell_to_check1 = self.worksheet.cell_value(1, 1)

        self.assertEqual(self.cell_to_check1, str(['PlaceHolder']))

    def test_check_wrongful_assignment(self):
        self.all_employees[6].employee_limits.append('Sunday Morning')
        self.all_shifts[0].assigned_employees.append(self.all_employees[6])
        self.all_shifts[0].assigned_names.append(self.all_employees[6].name)
        run()
        check_wrongful_assignment()
        self.assertIn('PlaceHolder', self.all_shifts[0].assigned_names)

