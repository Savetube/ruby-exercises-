# String Formatting
# This prints out "Hello, John!"
name = "John"
print ("Hello, %s!" % name)

print ("\n         =====\n")
# This prints out "John is 23 years old."
name = "John"
age = 23
print ("%s is %d years old." % (name, age))

print ("\n         =====\n")
# This prints out: 'A list: [1,2,3]'
mylist = [1,2,3]
print ("A list: %s" % mylist)

print ("\n         =====\n")
# printing with elements from arrays
# This prints out: "Hello John Doe. Your current balance is $53.44."
data = ["John","Doe",53.44]
format_string = ["Hello", "Your current balance is $"]
print("%s %s %s. %s%.2f." % (format_string[0],data[0],data[1],format_string[1],data[2]))

# and this alternative is using f-string
print (f"{format_string[0]} {data[0]} {data[1]}. {format_string[1]}{data[2]}.")

# alternative simple code is below.
data = ("John","Doe",53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."
print (format_string % data)

# this code is an alternative.
format_string = "Hello %s %s. Your current balance is $%s."
print (format_string % data)

print ("\n         =====\n")
# This shows the f-string function printing: 'from London to Paris'
origin = "London"
destination = "Paris"
print (f"from {origin} to {destination}")
