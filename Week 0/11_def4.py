# Define the main function that will execute the main logic of the program
def main():
    # Prompt the user for their name and store the input in the variable 'name'
    name = input("What's your name ? ")

    # Call the 'hello' function, passing the user's name as an argument
    hello(name)

    # Call the 'hello' function without any arguments, which will use the default value "world"
    hello()

# Define the 'hello' function that takes one optional parameter 'to'
# If no argument is provided, 'to' defaults to "world"
def hello(to="world"):
    # Print a greeting message that includes the name passed to the function
    print("Hello,", to)

# Call the main function to start the program
main()
