# Function to get the user's guess
def get_guess():
    # Prompt the user to enter a number and convert it to an integer
    guess = int(input("Enter your number: "))
    return guess  # Return the entered number

# Main function to execute the guessing game logic
def main():
    guess = get_guess()  # Call the get_guess function to get the user's input
    # Check if the guess matches the target number
    if guess == 50:
        print("Correct!")  # Print "Correct!" if the guess is 50
    else:
        print("Incorrect!")  # Print "Incorrect!" for any other guess

# Call the main function to start the program
main()

