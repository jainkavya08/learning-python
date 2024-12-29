def convert(input):
    return input.replace(":)" , "🙂").replace(":(" , "🙁")

def main():
    faces = input ("Enter your text : ")
    result = convert(faces)
    print(result)

main()
