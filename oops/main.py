
class Person:
    def __init__(self, name):
        self.name = name 

    def display(self):
        print("Name of Person is {}".format(self.name))

    def isemployee(self):
        print("Not a Employee")


# child class
class Employee(Person):
    def __init__(self, name, salary, post):
        Person.__init__(self, name,)
        self.__salary = salary
        self.post = post

    def isemployee(self):
        print("I am {} Employee".format(self.post))

    def increment(self):
        print(self.__salary * 2)


class Employee2(Person):
    def __init__(self, name,  salary, post):
        super().__init__(name)
        self.salary=salary 
        self.post=post 

    def isemployee(self):
        print("I am {} Employee".format(self.post))
        


person_obj1 = Person("Sai")
person_obj1.display()
person_obj1.isemployee()
person_obj2 = Employee('Rahul', 20000, "Intern")
person_obj2.display()
person_obj2.isemployee()
#print(a.__salary)
#print(a.post)
person_obj3 =Employee2("Teja",30000,"software Engineer")
person_obj3.display()
person_obj3.isemployee()


