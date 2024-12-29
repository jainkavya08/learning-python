def main():
    x = int (input("what's x? "))
    if Is_even(x):
        print("even")
    else:
        print ("odd")
def Is_even(n):
    return True if n % 2 == 0 else False

main()