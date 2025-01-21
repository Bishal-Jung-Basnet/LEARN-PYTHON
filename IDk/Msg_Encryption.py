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
#call main function to run
encoder()
def decoder():
    print("\nConverts unicode to text:")
    inString = input("Enter the unicode encoded message: ")
    #loop through each substring and build unicode message
    DecodedMessage =""
    for numStr in inString.split():
        #convert the (sub)string to a number
        codeNum= int(numStr)
        #append character to messgae
        DecodedMessage += chr(codeNum)
    print("The decpded message is:", DecodedMessage)
decoder()