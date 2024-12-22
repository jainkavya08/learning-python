# Ask the user for their name
name = input("What's your name? ").strip().title()

# If only you want to greet the person with their first name its good to use split
first , last = name.split (" ")

# Print the output
print(f"hello, {first}")