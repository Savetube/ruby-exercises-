# Subtitle: Functions
# keyword for functions is 'def'
def my_function():
    print("Hello From My Function!")
    
print("\n         =====\n")
# functions with arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))
    
print("\n         =====\n")
# functions return a value to the caller
# using the keyword 'return'
def sum_two_numbers(a,b):
    return a + b

print("\n         =====\n")
# calling function is simply by typing
# the function`s name followed by '()'

# Prints (a simple greeting)
my_function()

print("\n         =====\n")
# Prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

print("\n         =====\n")
# After this line x will hold the value 3!
x = sum_two_numbers(1,2)

print("\n         =====\n")
# Main Exercise
# Use existing functions while adding
# your own to create a fully functional
# program.
