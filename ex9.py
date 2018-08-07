# Subtitle: FUNCTIONS
# this is one of the exercises following the website: www.learnpython.org
1
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
# 1.) Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# 2.) Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with a string " is a benefit of functions!"
# 3.) Run and see all the functions work together!

# Exercises starts here
# define the function that list the benefits
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# A function that concatenates to each benefit the string " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit
    
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
    
name_the_benefits_of_functions()
