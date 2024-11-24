def encoder():
    print("This program converts a text message tnto a sequence")
    print("of numbers representing the unicode encoding.\n")

    #get tect to encode
    message = input("Please enter any message to encode: ")
    print("\nHere are the Unicode codes: ")

    #loop through the message and print out the unicode value
    for ch in message:
        print(ord(ch), end=" ")
print() 
#call main function
encoder()