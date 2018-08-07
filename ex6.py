# Subtitle: Basic String Operations
# this is one of the exercises following the website: www.learnpython.org

astring = "Hello World!"
astring2 = 'Hello World!'
print (astring + astring2)

print ("\n         =====\n")

astring = "Hello World!"
print ("single quotes are ' '")

print (len(astring))

print ("\n         =====\n")

print (astring.index("o"))

print ("\n         =====\n")

print (astring.count("l"))

print ("\n         =====\n")

print (astring[3:7])

print (astring[:7])

print (astring[-11:-4])

print ("\n         =====\n")

print (astring[3:7:2])
print (len(astring[3:7:2]))

print ("\n         =====\n")

# Below prints same output
# The general form is 
#     string_array[start:stop:step]
#
print (astring[3:7])
print (astring[3:7:1])

print ("\n         =====\n")

# Reverse printing
print (astring[::-1])

print ("\n         =====\n")

# This shows conversion to lower case or upper case
print (astring.upper())
print (astring.lower())

print ("\n         =====\n")

# Boolean checking whether starting and ending with specific string. returns 'true' or xfalse'.
print (astring.startswith("Hello"))
print (astring.startswith("hello"))
print (astring.endswith("wOrld!"))
print (astring.endswith("World!"))

print ("\n         =====\n")
#    This splits the string into a bunched of strings grouped together in a list. This used the character space as separator.
print (astring.split(" "))

#    This split using chracter 'l'
print (astring.split("l"))

print ("\n         =====\n")

#    Main Exercise
# Try to fix the code to point out the correct information by changing the string.
#s = "Hey there! What should this string be?"
s = "Strings are awesome!"
# Length should be 20
print ("Length of string = %d" % len(s))

# First occurrence of "a" should be at index 8.
print ("The first occurrence of the letter 'a' = %d" % s.index("a"))

# Number of a's should be 2
print ("a occurs %d times" % s.count("a"))

# # Slicing the string into bits
print ("The first five characters are '%s'" % s[:5]) # Start to to five
print ("The next five characters are '%s'" % s[5:10]) # 5 to 10
print ("The thirteenth character is '%s'" % s[12]) #Just number 12
print ("The chatacters with odd index are '%s'" % s[1::2]) # (0-based indexing)
print ("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print ("String in uppercase: '%s'" % s.upper())

# Convert everything to lowercase
print ("String in lowercase: '%s'" % s.lower())

# Check how the string start
if s.startswith("Str"):
    print ("String starts with 'Str'. Good.")
    
# Check how the string ends
if s.endswith("ome!"):
    print ("String ends with 'ome!'. Good.")
    
# Split the string into three separate strings, 
#each containing only a word.
print ("Split the words of the string: %s" % s.split(" "))
