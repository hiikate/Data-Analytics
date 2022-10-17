# Pet Class

class Pet:
    pass
    animals = 'pet'
# initializer
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

# instantiate the pet object
p1 = Pet("Fastie", "Dog", 8)
p2 = Pet("Lily", "Cat", 10)
p3 = Pet("Blue", "Bird", 5)

print(p1.name, "is a", p1.animal_type, "its", p1.age,"years old")
print(p2.name, "is a", p2.animal_type, "its", p2.age,"years old")
print(p3.name, "is a", p3.animal_type, "its", p3.age,"years old")