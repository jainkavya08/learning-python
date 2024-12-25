#Ask the user for input
name = input("What's your name ? ").strip().title()   #strip --> eliminates whitespace #title --> Captilizes

#If only you want to green the user with their first of last name then use split
first , last = name.split(" ")

#Print the output
print (f"Hello,{first}")

