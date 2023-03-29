class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def person_work(self, employ):
        print("{} is a {} ".format(self.name, employ))


class Employ(Person):
    def __init__(self, id, name, salary, gender):
        super().__init__(name, gender)
        self.id = id
        self._salary = salary

    def speak(self):
        print(self.name)


person1_obj = Person("sai", "male")
person1_obj.person_work("intern")

person2_obj = Employ(1,"reddy",20000,"male")
person2_obj.person_work("software Enigneer")
#person2_obj.speak()