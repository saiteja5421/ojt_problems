class Animal:
    def __init__(self):
        pass 

    def speak(self):
        print("It's Animal class")

class Dog(Animal):

    def speak(self):
        print("Dog shouts bow bow")

class Cat(Animal):

    def speak(self):
        print("cat shouts meow meow")
    
Animal_obj = Animal()
Animal_obj.speak()

Dog_obj =Dog()
Dog_obj.speak() 

Cat_obj =Cat()
Cat_obj.speak()