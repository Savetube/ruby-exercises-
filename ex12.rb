print "Give me a number: "
number = gets.chomp.to_i

puts "\nthe item you've just entered was directly converted to #{number.class} data type using one line of code."

bigger = number * 100
puts "A bigger number is #{bigger}."
puts "\n"
print "Give me another number: "
another = gets.chomp
puts "the next one you've just entered was not converted and is of #{another.class} data type."

number = another.to_i
puts "but another line of code converted it to #{number.class}."

smaller = number / 100
puts "A smaller number is #{smaller}."

bill = 103.40
puts "Please pay for my phone bill of #{bill}."
puts "I will pay you 10% interest ($#{bill * 0.1}) at the end of the month."
puts "I will forward to your bank account the total amount of $#{bill + (bill * 0.1)}."
 