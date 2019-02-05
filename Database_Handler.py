import mysql.connector as sqlcon
import WorkScheduler10


class DbHandler:

    def __init__(self):

        self.connection = sqlcon.connect(host='localhost', user='zem', password='Zemer123!@#', database='scheduler')
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(dictionary=True)

    def show_all_employees(self):
        self.cursor.execute('SELECT * FROM employee')
        data = self.cursor.fetchall()
        for row in data:
            print(row)

    def db_insert_employee(self, employee_first_name, employee_last_name):
        self.cursor.execute('INSERT INTO employee (employee_first_name, employee_last_name) VALUES (%s, %s)',
                            (employee_first_name, employee_last_name))
        self.connection.commit()

    def db_delete_employee_by_name(self, employee_first_name, employee_last_name):
        self.cursor.execute('DELETE FROM employee WHERE employee_first_name=%s AND employee_last_name=%s',
                            (employee_first_name, employee_last_name))
        self.connection.commit()

    def db_delete_employee_by_id(self, ids):
        self.cursor.execute('DELETE FROM employee WHERE ID="%s"', ids)
        self.connection.commit()

    def db_random_query(self, query, args):
        self.cursor.execute(query, args)
        self.connection.commit()

    def db_get_employee_names(self):
        self.cursor.execute('SELECT employee_first_name, employee_last_name FROM employee;')
        data = self.cursor.fetchall()
        for row in data:
            print(row)

    # def db_get_random_employee(self):
    #     self

    # def db_select_employee(self, authorization):
    #     self.cursor.execute('SELECT FROM employee_authorization')

    # def db_get_authorizations(self):
    #     authorization_dictionary = {}
    #     self.cursor.execute('SELECT idauthorization, authorization_name FROM authorization')
    #     data = self.cursor.fetchall()
    #     # print(data)
    #     # for row in data:
    #     #     print(row)
    #     for a, b in data:
    #         authorization_dictionary[a] = b
    #     print(authorization_dictionary)

    def db_get_employees(self):
        self.cursor.execute('SELECT idemployee, employee_first_name, employee_last_name,'
                            ' contract_shift_amount FROM employee')
        data = self.cursor.fetchall()
        for a, b, c, d in data:
            print(a, b, c, d)
            WorkScheduler10.Employee(a, b, c, d)
        print(WorkScheduler10.all_employees)

    def db_employee_authorizations(self):
        self.cursor.execute('SELECT idemployee, idauthorization FROM employee_authorization')
        data = self.cursor.fetchall()
        for row in data:
            print(row)
        for employee in WorkScheduler10.all_employees:
            for a, b in data:
                if employee.idemployee == a:
                    employee.authorization = b

    def db_employee_limits(self):
        self.cursor.execute('SELECT idemployee, idshift FROM employee_limit')
        data = self.cursor.fetchall()
        for employee in WorkScheduler10.all_employees:
            for a, b in data:
                if employee.idemployee == a:
                    employee.employee_limits.append(b)



    def db_get_days(self):
        self.cursor.execute('SELECT idday, day_name FROM day')
        data = self.cursor.fetchall()
        for a, b in data:
            print(a, b)
            WorkScheduler10.Days(a, b)
        print(WorkScheduler10.all_days)

    def db_get_shifts(self):
        self.cursor.execute('SELECT idshift, shift_name, idday, shift_required_employees,'
                            'shift_required_authorizations FROM shift')
        data = self.cursor.fetchall()
        for a, b, c, d, e in data:
            WorkScheduler10.Shifts(a, b, c, d, e)
        print(WorkScheduler10.all_shifts)



    def __del__(self):
        # self.cursor.close()
        self.connection.close()


handler = DbHandler()
# print(allemployees)
# handler.db_insert_employee('emek', 'netanel')
# handler.show_all_employees()
# handler.db_delete_employee_by_id(ids=2)
# handler.db_delete_employee_by_name('emek', 'netanel')
# handler.show_all_employees()




