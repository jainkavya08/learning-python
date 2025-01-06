# Why was this else at the end?
# Ans --> If both the above condition are equated to false then eventually the last statement is conditioned to be true 
# that's why else is used and boolean expression needs to be used 

x = int(input ("What's x ? "))
y= int(input ("What's y ? "))

if x < y:    #Boolean Expression
    print ("x is less than y ")
elif x > y:
    print ("x is greater than y")
else:
    print ("x equals y ")