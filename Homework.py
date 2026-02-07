# create class
class Dog:

    # class attribute
    species = "Dog"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Dog class
wlo = Dog("wlo", 4)
sal = Dog("sal", 9)

# access the class attributes
print("Wlo is a {}".format(wlo.species))
print("sal is also a {}".format(sal.species))

# access the instance atributes
print("{} is {} years old".format( wlo.name, wlo.age))
print("{} is {} years old".format( sal.name, sal.age))