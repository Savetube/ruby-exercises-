first, second, third = ARGV

puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

puts "What was your place in the last championship game? "
answer = $stdin.gets.chomp
if answer=='first'
  puts "keep up the good work."
end