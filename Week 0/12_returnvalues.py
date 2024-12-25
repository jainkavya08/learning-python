# Define the main function that will execute the main logic of the program
def main():
    # Prompt the user to enter a value for x and convert it to an integer
    x = int(input("Enter the value of x: "))
    
    # Print the result of squaring x by calling the 'square' function
    print("x squared is", square(x))

# Define the 'square' function that takes one parameter 'n'
def square(n):
    # Return the square of the input number n
    return n * n

# Call the main function to start the program
main()