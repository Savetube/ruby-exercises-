first_name, middle_name, last_name = ARGV

if middle_name==0
puts "What is your middle name? "
middle_name = $stdin.gets.chomp
end

if last_name==0
puts "What is your last name? "
last_name = $stdin.gets.chomp
end

puts "Hi #{first_name}!"

puts "#{last_name} is your father's name, is that right?"
