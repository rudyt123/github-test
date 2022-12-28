# example to learn inheritance
# employee can access only learn , manager can access learn and learning and append it

class Person:
    
    def a_access_learning(append):
            with open('learning.txt','a') as learning_append:
                    return learning_append.write(append)
    
    def r_access_learn():
            with open('learn.txt','r') as l_em:
                print(l_em.read())
    
    def r_access_learning():
            with open('learning.txt','r') as ling_em:
                    print(ling_em.read())
    

class Employee(Person):

    def employee_display():
        Employee.r_access_learn()



class Manager(Person):

    def manager_display():
        Manager.r_access_learn()
        Manager.r_access_learning()

    def manager_append_file(append):
        Manager.a_access_learning(append)

emp = Employee
mng = Manager
print('\n' + '#Employee can only be shown learn.txt' +'\n')
emp.employee_display()

print('#Managers can be shown learning.txt and learn.txt' + '\n')
mng.manager_display()

append = input('append : '+'\n')
mng.manager_append_file(append)

print('#Managers can be shown learning.txt and learn.txt' + '\n')
mng.manager_display()
