class Animal:
    def eat(self):
        print("i can eat")

# inherit from Animal
class Dog(Animal):
    # override the eat method
    def eat(self):
        super().eat()
        print("i like to eat bones")
        
# create an object of the subclass
labrador = Dog()

labador.eat()