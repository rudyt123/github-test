# 2) Write employee class and create object to create multiple employees

class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id = id_number
        self.salary = salary

    def employees(self):
        print(f'''{self.name} 
id : {self.id}
salary : ${self.salary}
''')


try:
    workers = True
    while workers is True:
        full_name = input('full name:  ')
        worker_id = input('id:  ')
        wage = int(input('salary: $ '))
        employee = Employee(full_name, worker_id, wage)
        employee.employees()
except ValueError:
    print('invalid')
    workers = False
