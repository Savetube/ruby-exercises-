# Subtitle: CONDITIONS
# this is one of the exercises following the website: www.learnpython.org

# Expression comparison and evaluation 
x = 2
print (x == 2) # prints out True
print (x == 3) # prints out False
print (x < 3) # prints out True

print ("\n         =====\n")
# The "and" and "or" operators
name = "John"
age = 23
if name == "John" and age == 23:
    print ("Your name is %s, and you are also %d years old." % (name,age))
    printarg = (name,age)
    print ("Your name is %s, and you are also %d years old." % printarg)

print ("\n         =====\n")
# The 'in' operator. Use to check if an specified object exist within an iterable object container.
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
    
print ("\n         =====\n")
# Python indentation(4 spaces) instead of brackets
x = 2
if x == 2:
    print ("x equals two!")
else:
    print ("x does not equal to two.")

print ("\n         =====\n")
# The 'is' operator matches the instance of objects, not the values
x = [1,2,3]
y = [1,2,3]
print (x == y)
print (x is y)

print ("\n         =====\n")
# The "not" operator
# using 'not' before a boolean operator inverts it
print (not False) # prints out True
print ((not False) == False) # prints False

print ("\n         =====\n")
# Main Exercise
# Change the variables accordingly to make all if statements output true
# number = 10
# second_number = 10
# first_array = []
# second_array = [1,2,3]

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print ("1")
    
if first_array:
    print ("2")
    
if len(second_array) == 2:
    print ("3")
    
if len(first_array) + len(second_array) == 5:
    print ("4")
    
if first_array and first_array[0] == 1:
    print ("5")
    
if not second_number:
    print ("6")