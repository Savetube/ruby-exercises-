name = 'Zed A. Shaw'
age = 35 # not a lie in 2009
height = 74 # inches
weight = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

# unit conversion variables
inch_to_cm = 2.54 # cm/inch 
lbs_to_kg = 2.205 # lbs/kg

puts "Let's talk about #{name}."

# height in inches
#puts "He's #{height} inches tall."

# height in cm
puts "He's #{height * inch_to_cm} cm tall."

# weight in lbs
#puts "He's #{weight} pounds heavy."

# weight in kg
puts "He's #{weight / lbs_to_kg} kilograms heavy."
puts "Actually, that's not too heavy."
puts "He's got #{eyes} eyes and #{hair} hair."
puts "His teeth are usually #{teeth} depending on the coffee."

# this line is tricky, try to get it exactly right!"
puts "If I add #{age}, #{height * inch_to_cm}, and #{weight / lbs_to_kg}, I get #{age + height *inch_to_cm + weight / lbs_to_kg}."




