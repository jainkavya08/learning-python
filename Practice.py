def greet (input):
    if "hello" in input:
        return ("Hello , There ")
    else:
        return ("Sorry i dont know you ")


greetings = greet("hello")
print ("mhm, " + greetings)