#!/bin/bash
echo Hello World

# code for inserting strings to file
echo 1234567890 > File # writing string to "File".
exec 3<> File # Open "File" and assign fd 3 (file descriptor 3) to it.
read -n 4 <&3 # Read only 4 characters.
echo -n . >&3 # Write a decimal point there.
exec 3>&- # Close fd 3.
cat File # ==> output should show 1234.4567890
