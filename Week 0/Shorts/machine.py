# Side effect example using a global variable
emoticon = ">.<"  # Initial global emoticon

def main():
    global emoticon  # Access the global variable
    say("Is anyone here?")  # First message with initial emoticon
    emoticon = ":D"  # Update the global emoticon
    say("Yes, here I am")  # Second message with updated emoticon

def say(phrase):
    # Print the phrase combined with the current emoticon
    print(phrase + " " + emoticon)

main()  # Run the main function
