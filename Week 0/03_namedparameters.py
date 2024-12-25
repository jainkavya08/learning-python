# Ask user for their name

name = input ("What's your name ? ")
#changing the end == basically the print function in python denotes next line but here
#  end value has changed so the output is on the same line
print ("Hello,", end = "")
print (name)

################

name = input ("what's your name ? ")
#changing the sep
# By default, sep is a space (' '), but here it is set to an empty string (''),
# so no space is added between "Hello," and the user's name.
print ("Hello,", name , sep ="")
