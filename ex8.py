# Subtitle: LOOPS
# this is one of the exercises following the website: www.learnpython.org

# The "for" loop
# iterates over a given sequence
primes = [2,3,5,7]
for prime in primes:
    print (prime)

print("\n         =====\n")
# range and xrange
# prints out 0,1,2,3,4
for x in range (5):
    print (x)

print("\n         =====\n")

# prints out 3,4,5
for x in range (3, 6):
    print (x)
    
print("\n         =====\n")
# prints out 3,5,7
for x in range (3, 8, 2):
    print (x)

print("\n         =====\n")
# The "while" loops
# repeats as long as a certain boolean
# condition is met
# prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 # This is the same as 'count = count + 1'
    
print("\n      =='break'==\n")
# "break" and "continue" statements
# 'break' is used to exit a for loop or
# a while loop. whereas 'continue' is
# used to skip the current block and
# return to the "for" or "while" statement.

#prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >=5:
        break

print("\n         =='continue'==\n")
# prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

print("\n             =='sleep'==\n")
from time import sleep
for x in range(10):
    # Check if x is not even
    if x % 2 != 0:
        print(x)
        sleep(0.2)
        continue
    print(x)
    sleep(0.4)
    
print ("\n            =='else'==\n")
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count < 5):
    print(count)
    sleep(0.5)
    count += 1
else:
    print("count value reached %d" % count)

print ("\n         =====\n")
# Prints out 1,2,3,4
for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else :
    print("This is not printed because for loop is terminated because of break but not due to fail in condition.")

print ("\n         =====\n")
# Main Exercise
# Loop through and print out all the
# numbers from the numbers list in the
# same order they are received. Don't print any numbers that come after 237 in the sequence.
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
for i in numbers:
    if i == 237:
        break
    elif (i % 2 != 0):
        continue
    print(i)
    sleep(0.2)


print("\n         =====\n")
    
# The other solution is shown below
for number in numbers:
    if number == 237:
        break
    
    if (number%2 == 1):
        continue
    sleep(0.1)
    print(number)