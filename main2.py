class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        # Call the speak method from Animal and print the additional message
        super().speak()
        print("and Woof!")

# Usage
my_dog = Dog()  # creating an instance of a dog class
my_dog.speak()  # This will print both messages