def hello(to="World"):
    # Print a greeting message that includes the name passed to the function
    print("Hello,", to)

# Prompt the user for their name and store the input in the variable 'name'
name = input("What's your name? ")

# Call the 'hello' function without any arguments, which will use the default value "World"
hello()

# Call the 'hello' function, passing the user's name as an argument
hello(name)
