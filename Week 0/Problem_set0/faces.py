# First define convert and take input as parameter and replace as parameters arguements
def convert (input):
    return input.replace(":)", "🙂").replace(":(", "🙁")

def main():
    faces = input("Enter your text : ")    #input from user
    result = convert(faces)         #calling the function convert 
    print(result)       # print the result

main()
