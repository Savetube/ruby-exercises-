formatter = " %{first} %{second} %{third} %{fourth}"

formatter2 = "%{first}
%{second}
%{third}
%{fourth}"

puts formatter2 % {first: 1, second: 2, third: 3, fourth:4}
puts formatter2 % {first: "one", second: "two", third: "three", fourth: "four"}
puts formatter2 % {first: true, second: false, third: true, fourth: false}
puts formatter2 % {first: formatter, second: formatter, third: formatter, fourth: formatter}

puts formatter2 % {
first: "I had this thing.",
second: "That you could type up that right.",
third: "But it didn`t sing.",
fourth: "So I said goodnight."
}