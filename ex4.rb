# assign value to variable cars
cars = 100

# assign the value for car capacity
space_in_a_car = 4.0

# declare the number of passengers
drivers = 30

# declare the number of passengers
passengers = 90

# declare the number of cars not in use
cars_not_driven = cars - drivers

# declare ghe number of cars driven
cars_driven = drivers

# declare the carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# declare the value for the number of passengers per car
average_passengers_per_car = passengers / cars_driven

puts "There are #{cars} cars available."
puts "There are only #{drivers} drivers available."
puts "There will be #{cars_not_driven} empty cars today."
puts "We can transport #{carpool_capacity} people today."
puts "We have #{passengers} to carpool today."
puts "We need to put about #{average_passengers_per_car} in each car."
