myint = 7
print (myint)

print ("\n=====\n")

myfloat = 7.0
print (myfloat)
myfloat = float(7)
print (myfloat)

print ("\n=====\n")

mystring = 'hello'
print (mystring)
mystring = "hello"
print (mystring)

print ("\n=====\n")

mystring = "Don't worry about aposthropes"
print (mystring)

print ("\n=====\n")

one = 1
two = 2
three = one + two
print (three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print (helloworld)

print ("\n=====\n")

a, b = 3,4
print (a,b)

print ("\n=====\n")

# The below will not work!
one = 1
two = 2
hello = "hello is not int"
if isinstance(hello, int):
   print (one + two + hello)
else:
   print (hello)
   
print ("\n=====\n")

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
   print("string: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
   print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
   print("Integer: %d" % myint)
   
print ("\n=====\n")