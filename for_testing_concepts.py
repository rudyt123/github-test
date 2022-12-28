# A simple Person class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'People(' + self.name + ',' + str(self.age) + ')'
        return rep


# Let's make a Person object and print the results of repr()

person = Person("John", 20)
print(person.__repr__())





li_ev = []
li_odd = []
for x in range(100):
    if x % 2 == 0:
        li_ev.append(x)
        
    else: 
        li_odd.append(x)

print(li_odd)





























