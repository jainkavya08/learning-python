# Function to generate a response based on input
def greet(input):
    # Check if "hello" is in the input
    if "hello" in input:
        return "Hello, there"  # Respond with a greeting
    else:
        return "Sorry, I don't quite understand"  # Default response

# Call the greet function with "hello"
greeting = greet("hello")
# Print the response with "kavya"
print(greeting + " kavya")
