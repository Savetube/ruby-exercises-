# Subtitle: CLASS
# this is one of the exercises following the website: www.learnpython.org
class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class.")
        
myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()
myobjecty.function()

print("\n         =====\n")
# Main Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car2.name = "Jump"
car1.kind = "convertible"
car2.kind = "van"
car1.color = "red"
car2.color = "blue"
car1.value = 60000
car2.value = 10000

# test code
print(car1.description())
print(car2.description())
    
#print("\n         =====\n")

#print("\n         =====\n")

#print("\n         =====\n")

