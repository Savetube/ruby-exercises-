# Subtitle: DICTIONARIES
# this is one of the exercises following the website: www.learnpython.org

# A database of phone numbers could be stored as follows:
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

print("\n         =====\n")
# alternatively, a phonebook database can be initialized with the ff notation:
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

print("\n         ==Iterations==\n")
# Iterating key value pairs using the below syntax:
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

    
#print("\n         =====\n")

